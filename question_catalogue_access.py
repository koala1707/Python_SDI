import json
""" holds original questions and provide the information to Question Answering Manager """
class QuestionCatalogueAccess:
    def __init__(self, file):
        self.questions = self.load_json(file)

    # loads contexts of the faq.json file.
    def load_json(self, file):
        json_file = open(file,"r")
        json_dict = json.load(json_file)
        return json_dict