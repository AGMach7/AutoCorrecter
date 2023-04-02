"""
string_manipulation module

This module provides functions for manipulating strings, including deleting, switching, replacing, and inserting characters.

Functions
-----------
    - delete_letter(word, verbose=False):
        Generate all possible words obtained by deleting one character from the input word.
        
        Parameters:\n
            - word (str): The input string/word.
            - verbose (bool): Whether to print additional information. Defaults to False.
            
        Returns:
            A list of all possible strings obtained by deleting one character from the input word.
            
            
    - switch_letter(word, verbose=False):
        Generate all possible words where one adjacent character is switched.
        
        Parameters:\n
            - word (str): The input string/word.
            - verbose (bool): Whether to print additional information. Defaults to False.
            
        Returns:
            A list of all possible strings with one adjacent character switched.
            

    - replace_letter(word, verbose=False):
        Generate all possible words where one letter from the original word is replaced.
        
        Parameters:\n
            - word (str): The input string/word.
            - verbose (bool): Whether to print additional information. Defaults to False.
            
        Returns:
            A list of all possible strings where one letter from the original word is replaced.
            

    - insert_letter(word, verbose=False):
        Generate all possible words obtained by inserting one character at every offset.
        
        Parameters:\n
            - word (str): The input string/word.
            - verbose (bool): Whether to print additional information. Defaults to False.
            
        Returns:
            A set of all possible strings obtained by inserting one character at every offset.
"""

def delete_letter(word, verbose=False):
    '''
    Generate all possible words obtained by deleting 1 character from word.

    Parameters
    -----------
    - word: the string/word for which you will generate all possible words 
                in the vocabulary which have 1 missing character

    Return
    -----------
    - delete_l: a list of all possible strings obtained by deleting 1 character from word
    '''
    
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    delete_l = [l+r[1:] for l,r in split_l if r]

    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")

    return delete_l

def switch_letter(word, verbose=False):
    '''
    Generate all possible strings with one adjacent character switched.

    Parameters
    -----------
    - word: input string

    Return
    -----------
    - switches: a list of all possible strings with one adjacent charater switched
    '''
    
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    switch_l = [l+r[1]+r[0]+r[2:] for l,r in split_l if len(r)>1]
    
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}") 

    return switch_l

def replace_letter(word, verbose=False):
    '''
    Generate all possible strings where we replaced one letter from the original word.

    Parameters
    -----------
    - word: the input string/word.

    Return
    -----------
    - replaces: a list of all possible strings where we replaced one letter from the original word. 
    ''' 
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    replace_l = [l+i+r[1:] for l,r in split_l for i in letters if r and (l+i+r[1:] != word)]
    
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l = {replace_l}")   
    
    return replace_l

def insert_letter(word, verbose=False):
    '''
    Generate all possible words obtained by inserting 1 character from word.

    Parameters
    -----------
    - word: the input string/word.

    Return
    -----------
    - inserts: a set of all possible strings with one new letter inserted at every offset
    ''' 
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    insert_l = [l+i+r for l,r in split_l for i in letters]

    if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
    
    return insert_l