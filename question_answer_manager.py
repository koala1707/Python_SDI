# from interactive_console_client import InteractiveConsoleClient
from question_log_access import QuestionLogAccess
from maching_engine import MachingEngine
class Candidate:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

class QuestionAnswerManager:
    def answer_question(self,text):
        user_question = text;
        QuestionLogAccess.store_user_input(user_question)
        answer_json,score = MachingEngine.get_maching_answer(user_question)
        return Candidate(answer_json['question'],answer_json['answer']), score