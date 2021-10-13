import json


class QuestionCatalogueAccess:
    def load_json():
        json_file = open("faq.json","r")
        json_dict = json.load(json_file)
        # print(json_dict)
        # print(json_dict[0].keys())
        # all_questions = []
        # for entry in json_dict:
        #     all_questions.append(entry["question"])
        return json_dict


    # print(load_json())    
    
    # def get_answer_from_json(number):
