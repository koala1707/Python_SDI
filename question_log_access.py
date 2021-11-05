# Stores the user input in the Asked Questions Store
class QuestionLogAccess:
    def __init__(self,filename):
        self.filename = filename

    # When the system gets user questions,
    # store the questions in a text file (asked_question_log.txt).
    def store_user_input(self, question):
        if question != "" or question != None:
            question_file = open(self.filename,"a")
            question_file.write(f"{question}\n")
            question_file.close()
            