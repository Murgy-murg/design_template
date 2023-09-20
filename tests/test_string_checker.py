import pytest
from lib.string_checker import *
def test_if_argument_contains_hastag_TODO_then_return_True():
    expected = True
    actual = string_checker('#TODO fix washing machine')
    assert actual == expected

def test_if_string_contains_string_with_hashtag_TODO_at_different_index_return_true():
    expected = True
    actual = string_checker('clean carpet, #TODO')
    assert actual == expected

def test_if_string_contains_hastag_TODO_not_all_upper_case_return_False():
    expected = False
    actual = string_checker('#ToDo fix washing machine')

def test_if_string_contains_no_hashtag_TODO_then_return_False():
    expected = False
    actual = string_checker('TODO fix washing machine')
    assert actual == expected
    
def test_if_argument_is_not_string_return_error_message():
    expected = 'Input must be a string!'
    with pytest.raises(Exception) as e:
        string_checker(123)
    actual = str(e.value)
    assert actual == expected

def test_if_list_containt_hashtag_TODO_then_return_True():
    expected = True
    actual = string_checker(['clean carpet', 'do dishes', '#TODO fix washing machine'])
    assert actual == expected
