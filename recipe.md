As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

def string_checker(string):
    """Ensure that string or contains given substring with value #TODO

    Parameters: (A string of words or a of strings)
        mixed_words: a string or containing the string #TODO

    Returns: (True False value)
        True or False value depending on whether conditions are met

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.

    """


Given an argument (list or string) if the argument contains #TODO then return true
"""
sstring_checker('#TODO fix washing machine') => True

"""
Given an argument (list or string) if the argument contains #TODO at different index than the start of string then return true
"""
string_checker('add fix washing machine to #TODO list') >= True

"""
Given an arguemnt (list or string) if the argument contains #Todo (Not all uppercase) then return False
"""
string_chekcer('#ToDo fix washing machine) >= False

"""
Given argument (string or list) if the argument contains 'TODO' then return false
"""
string_checker('TODO fix washing machine') >= False

"""
Given a non string or list type as argument, then return error message
"""
string_checker(123) >= "Input must be a string or list!"

"""
