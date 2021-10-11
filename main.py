from interactive_console_client import InteractiveConsoleClient
from question_answer_manager import QuestionManager
from question_catalogue_access import QuestionCatalogueAccess
import utils
import json
import os

def main(candidates_path, questions_log_path):
    #TODO your initialization code goes here, replacing the `manager = None` statement
    #
    # manager = None

    #example 'Question Log Access' write function
    question = "What day is today?"
    question_file = open("asked_questions_log.txt","w")
    question_file.write(question)
    question_file.close()
    
    
    
    manager = QuestionManager()
    QuestionCatalogueAccess()

    client = InteractiveConsoleClient(manager)
    question = client.run()

    # utils.text_to_words(question)
    # https://www.w3schools.com/python/python_ref_dictionary.asp
    json_file = open("faq.json","r")
    json_dict = json.load(json_file)
    print(json_dict[0].keys())
    all_questions = []
    for entry in json_dict:
        all_questions.append(entry["question"])
    print(all_questions)




if __name__ == '__main__':
    print('Module Name: {}'.format(__name__))
    main("faq.json", "asked_questions_log.txt")
