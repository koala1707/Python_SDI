from question_log_access import QuestionLogAccess
from maching_engine import MachingEngine

# Return the original question and answer to given the user question.
class Candidate:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

class QuestionAnswerManager:
    # The user enters a question 
    def answer_question(self,text):
        # Store the given user question
        QuestionLogAccess.store_user_input(text)
        # Look up the most similar question in the system to the given user question
        answer_json,score = MachingEngine.get_maching_answer(text)
        # if similar question exists
        if score != 0:
            # return the question and its associated answer to the user
            return Candidate(answer_json['question'],answer_json['answer']), score
        # no a similar question
        return answer_json, score
        