"""
data_preprocessing module

This module provides functions for processing the data, counting the words, and calculating their probabilities.

Functions:
-----------
    - process_data(file_name):
        Read a text file and return a list of words in lower case.
        - file_name: The name of the file to read from the current directory.
        - words: A list containing all the words in the corpus (text file) in lower case.
        - FileNotFoundError: If the specified file cannot be found.

    - get_count(word_l):
        Create a dictionary where keys are the words and values are their frequencies.
        - word_l: A list or tuple of words representing the corpus.
        - word_count_dict: A dictionary where the keys are the words and the values are their frequencies.
        - TypeError: If the input is not a list or tuple.

    - get_probs(word_count_dict):
        Create a dictionary where keys are the words and values are their probabilities.
        - word_count_dict: A dictionary where the keys are the words and the values are their frequencies.
        - probs: A dictionary where the keys are the words and the values are their probabilities.
        - TypeError: If the input is not a dictionary.

Note:
-----------
    This module assumes that the input text file is encoded in UTF-8 and that words are separated by whitespace characters.
    Non-alphanumeric characters, such as punctuation marks, are ignored and not counted as words.

"""

import re
from collections import Counter

def process_data(file_name):
    """
    Read a text file and return a list of words in lower case.

    Parameters
    -----------
    - file_name: The name of the file to read.

    Return
    -----------
    - words: a list containing all the words in the corpus in lower case.

    Errors
    -----------
    - FileNotFoundError: If the specified file cannot be found.
    """
    try:
        with open(file_name) as file:
            df = file.read().lower()
            words = re.findall('\w+', df)
        return words
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_name}' not found.")


def get_count(word_l):
    """
    Create a dictionary where keys are the words and values are their frequencies.

    Parameters
    -----------
    - words: A list of words representing the corpus.

    Return
    -----------
    - A dictionary where key is the word and value is its frequency.
    
    Error
    -----------
    - TypeError: If the input is not a list.
    """

    if not isinstance(word_l, (list, tuple)):
        raise TypeError(f"Input must be a list or tuple, got {type(word_l)} instead.")
    
    return Counter(word_l)

def get_probs(word_count_dict):
    """
    Create a dictionary where keys are the words and values are their probabilities.

    Parameters
    -----------
    - word_count_dict: The dictionary where key is the word and value is its frequency.

    Return
    -----------
    - probs: A dictionary where keys are the words and values are their probabilities.
    
    Error
    -----------
    - TypeError: If the input is not a dictionary.
    """

    if not isinstance(word_count_dict, dict):
        raise TypeError(f"Input must be a dictionary, got {type(word_count_dict)} instead.")

    total_words = sum(word_count_dict.values())
    probs = {word: count / total_words for word, count in word_count_dict.items()}
    
    return probs