from question_catalogue_access import QuestionCatalogueAccess
import utils
# Computes the most similar question and answer pair for user input.
class MachingEngine:
    # get an original question and answer to given a user question.
    def get_maching_answer(text):
        # list of the user input without punctuations
        user_question = utils.text_to_words(text)
        # convert all words to lowercase
        lower_user_question = utils.words_to_lowercase(user_question)
        # get an original question and answer from the faq.json file.
        origin_question = QuestionCatalogueAccess.load_json()
        # comparison with given a user input and stored a system question 
        most_similarity = 0
        final_answer = ""
        for question_answer in origin_question:
            # list of the system question without puncuations
            origin_question_list = utils.text_to_words(question_answer['question'])
            # convert all words to lowercase
            lower_origin_question = utils.words_to_lowercase(origin_question_list)
            # comparison with given a user input and stored a system question
            similarity = utils.jaccard_similarity_score(lower_origin_question, lower_user_question)
            # if similarity is larger than most_similarity, most_similarity is updated to the one.
            if most_similarity < similarity:
                most_similarity = similarity
                # When finding the most similar question to given the user input, final_answer holds the most similar question in the faq.json file (system).
                final_answer = question_answer
        return final_answer, most_similarity


    def sample(test):
        test = "apple"
        if test == "apple":
            return True
        return False