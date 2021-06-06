# =============================================================================
#  Multiple Choice Quiz
#  Mr. Farren - May 2021
#
#  A MC quiz game about computing.
#  The game requires a text file called questions.txt to load up the game data.
#  =============================================================================
# Imports:
import sqlite3, os, random
from sqlite3 import Error

#Globals
NUM_OF_QUESTIONS = 3
CURR_DIR = os.path.dirname(os.path.realpath(__file__))  #Get the current directory for the .py

#DB Connection: Requires db file name as string, e.g. "myfile.db" RETURNS connection
def CreateConnection(db):
    #Create connection
    con = None
    try:
        con = sqlite3.connect(CURR_DIR + "/" + db)
    except Error as e:
        print(e)
    return con


#Create cursor to run SQL commands
def CountQuestions(con):
    try:
        cur = con.cursor()
        cur.execute("SELECT id FROM questions")
    except Error as e:
        print(e)
    finally:
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Table is empty")
        else:
            # cur.close()
            return rows

# Show Question
def ShowQuestion(con, i):
    i = int(i)
    try:
        cur = con.cursor()
        cur.execute("""SELECT Question, CorrectAnswer, WrongAnswer1, WrongAnswer2, WrongAnswer3 
                        FROM questions 
                        WHERE ID=?""", (i, )) #Get ONE question
    except Error as e:
        print(e)
    finally:
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Table is empty")
        else:
            # cur.close()
            return rows

def ShowAnswers(i,q):
    #Get answers. Put in to list
    answers = []
    for j in range(1,5):        # 1 to 5 to cover tuple indexs 1 to 4. CorrectAnswer is index 1
        answers.append(q[0][j])     
    # print(answers)
    correctAnswer = answers[0]

    #Shuffle answers
    rs = random.sample(answers,4)
    for j in range(0,4):
        print("   ",j +1,"-",rs[j])

    return rs

def Play():
    #Connect to DB
    con = CreateConnection("Quiz.db")

    #Coutn questions
    qnum = CountQuestions(con)
    if qnum == None:
        print("ERROR: There are no questions in the database")

    # get/show question
    score = 0
    for i in range(0, len(qnum)):  #TODO: change len(qnum) to user choice of number of q's
        print()
        q = ShowQuestion(con,i+1)  #+1
        print(q[0][0])
        correctAnswer = q[0][1]
        # print("CA:",correctAnswer)
        rs = ShowAnswers(i,q)
        #Get input
        print()
        try:
            a = int(input("Your Answer: "))
        except:
            print("Must be a number")
        #check if correct answer
        if correctAnswer == rs[a - 1]:
            score += 1                       #Increment score
    print()
    print("Your score:", score)
    print()
    input("Press ENTER to return to the menu")

# =======================================
# MAIN PROGRAM
def main():
    print("""
    ***************************************
             Welcome to the quiz
        Enter: 
            P to PLAY
            A to enter ADMIN
            Q to QUIT
    ***************************************

    """)
    choice = input(" : ").upper()
    if choice == "P":
        Play()
    elif choice == "Q":
        print("Thanks for playing!")
        return choice

choice = "PLAY"
while choice != "Q":
    if __name__ == '__main__':
        choice = main()