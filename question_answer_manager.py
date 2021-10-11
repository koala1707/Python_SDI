class Candidate:
        def __init__(self,question,answer):
            self.question=question
            self.answer=answer

class QuestionManager:
    def answer_question(self,text):
        print("You wrote {}".format(text))
        return Candidate("question","Erika"), 10