import json

class QuestionCatalogueAccess:
    def load_json():
        json_file = open("faq.json","r")
        json_dict = json.load(json_file)
        print(json_dict[0].keys())
        all_questions = []
        for entry in json_dict:
            all_questions.append(entry["question"])
        return "HERE" + all_questions