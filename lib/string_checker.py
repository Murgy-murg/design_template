def string_checker(string):
    if isinstance(string, str):
        if '#TODO' in string:
            return True
        else:
            return False 
    elif isinstance(string, list):
        for i in string:
            if '#TODO' in i:
                return True
        else:
            return False
    else:
        raise Exception('Input must be a string!')

    