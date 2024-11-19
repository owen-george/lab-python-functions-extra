def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    i = 0
    j = 0 
    for char in string:
        if char.isupper():
            i += 1
        elif char.islower():
            j += 1
    print(f"Uppercase count: {i}. Lowercase count: {j}")
    return (i,j)

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    import string
    
    new_str = ""
    for char in sentence:
        if char.isalpha() or char == " " or char.isdigit():
            new_str += char
    
    return new_str

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    cleaned_sentence = remove_punctuation_f(sentence)
    word_list = list(cleaned_sentence.split())
    return len(word_list)
    