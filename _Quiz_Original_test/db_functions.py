import sqlite3, os
from sqlite3 import Error

CURR_DIR = os.path.dirname(os.path.realpath(__file__))  #Get the current directory for the .py
# DB = CURR_DIR + "/Quiz.db"

def CreateConnection(db):
    #Create connection
    con = None
    try:
        con = sqlite3.connect(CURR_DIR + "/" + db)
    except Error as e:
        print(e)
    return con

con = CreateConnection("Quiz.db")

#Create questions table
# cur.execute("""CREATE TABLE 'questions' (
#                       'ID' INTEGER PRIMARY KEY,   #AUTOINCREMENT
#                       'Question'	TEXT NOT NULL,
#                       'CorrectAnswer' TEXT NOT NULL, 
#                       'WrongAnswer1'	TEXT NOT NULL, 
#                       'WrongAnswer2'	TEXT, 
#                       'WrongAnswer3'	TEXT, 
#                       """)

#Create cursor to run SQL commands
def ViewQuestionsTable():
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM questions")
    except Error as e:
        print(e)
    finally:
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Table is empty")
        else:
            print(rows)


# Insert a row of data
# try:
#     cur = con.cursor()
#     cur.execute("INSERT INTO questions VALUES (1, 'A mouse is an example of...', 'Hardware', 'Software', 'OS', 'Storage')")
# except Error as e:
#     print(e)

# con.commit()
# ViewQuestionsTable()
# con.close()

#Insert new question
def AddQuestion(con, question):
    try:
        cur = con.cursor()
        q = question
        cur.executemany("INSERT INTO questions(Question,CorrectAnswer,WrongAnswer1,WrongAnswer2,WrongAnswer3) VALUES (? , ?, ?, ?, ?)", q)
    except Error as e:
        print(e)
    finally:
        con.commit()
        con.close()
        

# Columns: Question,CorrectAnswer,WrongAnswer1,WrongAnswer2,WrongAnswer3
question = [
    ("What is the purpose of the CPU?", "To process data", "To count your money", "To store data", "To start the computer"),
    ("What is the connection between Windows, macOS, Ubuntu and Android?", "Operating systems","Chocolate bars","Software","Computer systems"),
]

# AddQuestion(con, question)
ViewQuestionsTable()
con.commit()
con.close()