--
-- File generated with SQLiteStudio v3.3.3 on Tue Jun 29 14:19:34 2021
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: quiz_question
DROP TABLE IF EXISTS quiz_question;

CREATE TABLE quiz_question (
    id               INTEGER       NOT NULL
                                   PRIMARY KEY AUTOINCREMENT,
    questionText     VARCHAR (240) NOT NULL,
    correctAnswer    VARCHAR (140) NOT NULL,
    incorrectAnswer1 VARCHAR (140) NOT NULL,
    incorrectAnswer2 VARCHAR (140) NOT NULL,
    incorrectAnswer3 VARCHAR (140) NOT NULL
);

INSERT INTO quiz_question (id, questionText, correctAnswer, incorrectAnswer1, incorrectAnswer2, incorrectAnswer3) VALUES (1, 'A mouse is an example of...', 'Hardware', 'Software', 'Data', 'Process');
INSERT INTO quiz_question (id, questionText, correctAnswer, incorrectAnswer1, incorrectAnswer2, incorrectAnswer3) VALUES (2, 'What is the purpose of the CPU?', 'To process data', 'To count your money', 'To store data', 'To start the computer');
INSERT INTO quiz_question (id, questionText, correctAnswer, incorrectAnswer1, incorrectAnswer2, incorrectAnswer3) VALUES (3, 'What is the connection between Windows, macOS, Ubuntu and Android?', 'Operating systems', 'Chocolate bars', 'Software', 'Computer systems');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
