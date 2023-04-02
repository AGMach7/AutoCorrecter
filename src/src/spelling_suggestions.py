"""
string_suggestions module

This module provides a function for suggesting possible corrections for a misspelled word.

Functions:
-----------
    - get_corrections(word, probs, vocab, n=5, verbose=False)\n
        Given a potentially misspelled word, a dictionary of probabilities, and a set of valid vocabulary words,\n
        returns a list of the n best suggested corrections for the word.


Arguments:
-----------
    - word: str\n
        The potentially misspelled word that needs correction suggestions.


    - probs: dict\n
        A dictionary that maps each word to its probability in the corpus. This information is used to suggest\n
        corrections that are more likely to appear in the corpus.


    - vocab: set\n
        A set containing all valid vocabulary words that can be suggested as corrections.


    - n: int, default=5\n
        Number of possible word corrections you want returned in the dictionary.


    - verbose: bool, default=False\n
        Whether to print debugging information to the console, such as the entered word and suggested corrections.

Returns:
-----------
    - n_best: list\n
        A list of n tuples, where each tuple contains a suggested corrected word and its corresponding probability\n
        (from the given `probs` dictionary). The list is sorted by probability in descending order.

        
Example Usage:
-----------
    >>> from string_suggestion import get_corrections
    >>> vocab = {'hello', 'world', 'how', 'are', 'you'}
    >>> probs = {'hello': 0.1, 'world': 0.05, 'how': 0.2, 'are': 0.15, 'you': 0.1}
    >>> word = 'hollo'
    >>> get_corrections(word, probs, vocab, n=3)
    [('hello', 0.1), ('how', 0.2), ('you', 0.1)]

"""

from edit_letters import *

def get_corrections(word, probs, vocab, n = 5, verbose = False):
    '''
    Parameters
    -----------
    - word: a user entered string to check for suggestions
    - probs: a dictionary that maps each word to its probability in the corpus
    - vocab: a set containing all the vocabulary
    - n: number of possible word corrections you want returned in the dictionary

    Return
    -----------
    - n_best: a list of tuples with the most probable n corrected words and their probabilities.
    '''
    suggestions = []
    n_best = []
    
    if (word in vocab) and word:
        suggestions.append(word)
    suggestions = list(edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(vocab))
    
    n_best = [[s,probs[s]] if s in probs.keys() else [s,0] for s in suggestions]
    n_best = sorted(n_best, key=lambda x: x[1], reverse=True)[:n]
    
    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best