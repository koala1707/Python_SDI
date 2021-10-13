from question_catalogue_access import QuestionCatalogueAccess
import utils
class MachingEngine:
    def get_maching_answer(text):
        user_question = utils.words_to_lowercase(utils.text_to_words(text))
        origin_question = QuestionCatalogueAccess.load_json()
        high_similarity = 0
        for i in origin_question:
            origin_question_list = utils.text_to_words(i['question'])
            lower_origin_question = utils.words_to_lowercase(origin_question_list)
            similarity = utils.jaccard_similarity_score(lower_origin_question, user_question)
            if high_similarity < similarity:
                high_similarity = similarity
                final_answer = i
        return final_answer, high_similarity