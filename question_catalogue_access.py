import json
# holds original questions and provide the information to Question Answering Manager
class QuestionCatalogueAccess:
    # loads contexts of the faq.json file.
    def load_json():
        json_file = open("faq.json","r")
        json_dict = json.load(json_file)
        return json_dict