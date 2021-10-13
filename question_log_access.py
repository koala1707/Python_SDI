# from question_answer_manager import QuestionAnswerManager
# from interactive_console_client import InteractiveConsoleClient
class QuestionLogAccess:

    def store_user_input(question):
        question_file = open("asked_questions_log.txt","a")
        question_file.write(f"{question}\n")
        question_file.close()
        
        

    store_user_input("how much")
    