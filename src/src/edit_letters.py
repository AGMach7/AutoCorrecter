"""
edit_letters module

This module provides functions for generating all possible words that are one or two edits away from a given word. 
An edit can be any one of the following operations: deleting a character, replacing a character, inserting a character, or switching two adjacent characters.

Functions:
-----------
    edit_one_letter(word, allow_switches=True):
        Generate all possible words obtained by editing 1 character from the input word.

        Input:
            word (str): The input word for which to generate all possible words that are one edit away.
            allow_switches (bool, optional): Whether or not to allow adjacent character switches. Default is True.

        Returns:
            set: A set of words with one possible edit. Returns an empty set if the input word is empty.

    edit_two_letters(word, allow_switches=True):
        Generate all possible words obtained by editing 2 characters from the input word.

        Input:
            word (str): The input word for which to generate all possible words that are two edits away.
            allow_switches (bool, optional): Whether or not to allow adjacent character switches. Default is True.

        Returns:
            set: A set of strings with all possible two edits. Returns an empty set if the input word is empty.

Example Usage:
-----------
    >>> import edit_letters

    >>> edit_one = edit_letters.edit_one_letter("hello")
    >>> print(edit_one) 
    # Output: {'helo', 'helloo', 'hellp', 'jello', 'hallo', 'helle', 'helol'}

    >>> edit_two = edit_letters.edit_two_letters("hello")
    >>>  print(edit_two) 
    # Output: {'hells', 'helo', 'hdllp', 'helloo', 'hellt', 'jello', 'hcllo', 'hallo', 'yello', 'helle', 
    # 'gello', 'helol', 'hpllo', 'hezlo', 'helpo', 'hsllo', 'hewlo', 'helln', 'hyllo', 'hellr', 'hedlo', 
    # 'heqlo', 'helloe', 'heloq', 'healo', 'helko', 'heslo', 'helvo', 'helfo', 'hkllo', 'hejlo', 'helxo', 
    # 'heldo', 'hullo', 'helmo', 'hellc', 'hillo', 'halo', 'helio', 'hell', 'hela'}

"""

from string_manipulations import *

def edit_one_letter(word, allow_switches = True):
    """
    Generate all possible words obtained by editing 1 character from word.

    Parameters
    -----------
    - word: the string/word for which we will generate all possible words that are one edit away. 

    Return
    -----------
    - edit_one_set: a set of words with one possible edit. Please return a set. and not a list.
    """
    
    edit_one_set = set()
    
    delete_l = delete_letter(word)
    replace_l = replace_letter(word)
    insert_l = insert_letter(word)
    switch_l = []
    if allow_switches:
        switch_l = switch_letter(word)
    edit_one_set = set(delete_l + replace_l + insert_l + switch_l)


    return edit_one_set

def edit_two_letters(word, allow_switches = True):
    '''
    Generate all possible words obtained by editing 2 characters from word.

    Parameters
    -----------
    - word: the input string/word 

    Return
    -----------
    - edit_two_set: a set of strings with all possible two edits
    '''
    
    edit_two_set = set()
    
    edit_one = edit_one_letter(word, allow_switches)
    for w in edit_one:
        edit_two = edit_one_letter(w,allow_switches)
        edit_two_set.update(edit_two)
    
    return edit_two_set