# Find all close matches of input string from a list
# Programme by parth.py
from difflib import get_close_matches

def close_matches(pattern, word):
    print(get_close_matches(word, pattern))

word = "apple"
pattern = ['aple','namndkefh','alepl','sdvdsvsd','appel']
close_matches(pattern, word)
"""
output:
['aple','appel','alepl']
"""