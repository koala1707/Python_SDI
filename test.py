import pytest

from maching_engine import MachingEngine
# from main


# TODO add your tests here
def test_get_maching_answer():
    assert MachingEngine.get_maching_answer("What day is today?") == ({'question':'What day is it today', 'answer': 'Monday'}, 0.5)
    assert MachingEngine.sample("apple") == True
    assert MachingEngine.sample("bana") == True
    