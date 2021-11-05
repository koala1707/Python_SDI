import pytest

from matching_engine import MatchingEngine
from question_answer_manager import QuestionAnswerManager, Candidate
from interactive_console_client import InteractiveConsoleClient
from question_catalogue_access import QuestionCatalogueAccess
from question_log_access import QuestionLogAccess

# from main
# TODO add your tests here


# fixtures
@pytest.fixture
def client():
    manager = QuestionAnswerManager("test.json","test.txt")
    return InteractiveConsoleClient(manager)

@pytest.fixture
def manager():
    return QuestionAnswerManager(json_file="test.json", question_log_filename="test.txt")

# test if get_matching_answer for matching_engine works to find a similar question for a user question
def test_get_matching_answer_with_exact_question():
    test_matchinEngine = MatchingEngine(QuestionCatalogueAccess("test.json"));
    assert test_matchinEngine.get_matching_answer("What day is it today?") == (
    {'question': 'What day is today?', 'answer': 'Monday'}, 0.8)
    
def test_get_matching_answer_with_fuzzy_question():
    test_matchinEngine = MatchingEngine(QuestionCatalogueAccess("test.json"));
    assert test_matchinEngine.get_matching_answer("Hello World") == ('', 0)
    
# test if load_json in question_catalogue_access.py works to load a json file
def test_load_json():
    assert QuestionCatalogueAccess("test.json").load_json("test.json") == ([{'question': 'What day is today?', 'answer': 'Monday'}])

# test if store_user_input in question_log_access.py works to store user inputs
def test_store_user_input():
    question = "What is it today?"
    assert QuestionLogAccess("test.txt").store_user_input(question) == None

def test_manager_with_exact_question(manager):
        candidate, _score = manager.answer_question("What day is today?")
        assert candidate.answer == "Monday"

def test_manager_with_fuzzy_question(manager):
        candidate, _score = manager.answer_question("What day is it?")
        assert candidate.answer == "Monday"
    
def test_manager_with_no_question(manager):
        candidate, _score = manager.answer_question("")
        assert candidate.answer == ""