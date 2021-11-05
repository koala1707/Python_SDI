# Overview
This is a simple system to return an answer (with a similar question) to a user question.
The system stores the user input and has stored original question-answer pairs for the user question.

# Requirements
Requires python <=3.8.9

# Run
main system: "python3 main.py" in the terminal
test: "pytest test_assignment.py" in the terminal

# Architecture
The system is composed of nine files excluding test files.
Although I explained the structure of this system at Report.pdf, I will desribe them shortly.
The "question_answer_manager.py" receives the user input and transfer the question to the "question_log_access.py" for the file to store it in the "asked_question_log.txt". 
And also, the file returns a question-answer pair to the user.
The "matching_engine.py" receives the user input from the question_answer_manager.py and looks for the similar a question-answer pair from the "question_catalogue_access.py" which holds some question-answer pairs as a json file ("faq.json").
("main.py": run the system, "interactive_console_client.py", "utils.py": include some methods to find a similar pair)

The test is composed of three files.
test_assignment.py, test.json and test.txt

