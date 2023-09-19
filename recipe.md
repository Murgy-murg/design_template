#As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

def sentence_modifyer(string):
    """Ensure first letter is capitalized and sentence is inded with correct puntuation

    Parameters: (A string of words)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (True False value)
        True or False value depending on whether conditions are met

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.

    """


Given a string of words, if first letter of string is capital and last index of string is suitable punctuation then return true.
"""
sentence ("Hello my name is samuel.") => True

"""
Given a string of words, if letter of string is capital but last index of string is not suitable puntuation then return False
"""
string_modifyer("Hello my name is samuel") >= False 

"""
Given a string of words, if first letter of string is not capital but last index is suitable punctuation then return False
"""
string_modifyer("hello my name is samuel.") >= False

"""
Given a string of words, if first letter of string is not capital and last index is not suitable punctuation then return False
"""
string_modifyer("hello my name is samuel") >= False

"""
Given a non string type as argument, then return error message
"""
string_modifyer(123) >= "Input must be a string!"

"""
