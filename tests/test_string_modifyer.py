from lib.string_modifyer import *
import pytest
def test_correct_string_returns_true():
    expected = True
    actual = string_modifyer('Hello my name is samuel.')
    assert actual == expected
def test_no_punctuation_at_end_of_string_returns_false():
    expected = False
    actual = string_modifyer('Hello my name is samuel')
    assert actual == expected
def test_no_capital_letter_at_start_of_string_returns_false():
    expected = False
    actual = string_modifyer('hello my name is samuel.')
    assert actual == expected
def test_no_capital_letter_or_punctuation_included_in_string():
    expected = False
    actual = string_modifyer('hello my name is samuel')
    assert actual == expected
def test_returns_error_if_input_is_not_string():
    expected  = 'Input must be a string!'
    with pytest.raises(Exception) as e:
        string_modifyer(123)
    actual= str(e.value)
    assert actual == expected
