# Stores the user input in the Asked Questions Store
class QuestionLogAccess:
    # When the system gets user questions, store the questions in a text file (asked_question_log.txt).
    def store_user_input(question):
        if question != "" or question != None:
            question_file = open("asked_questions_log.txt","a")
            question_file.write(f"{question}\n")
            question_file.close()
        
        

    