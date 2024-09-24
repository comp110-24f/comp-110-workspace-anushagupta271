"""Challenge Question 3 9/18"""

__author__ = "730646393"


def num_instances(phrase: str, search_char: str) -> int:
    """loops through each letter of phrase and counts each occurence of search_char in phrase"""
    i: int = 0  # index local var
    count: int = 0  # count local var
    while i < len(phrase):
        if search_char == phrase[i]:  # checks if search_char is at index of phrase
            count = count + 1
            # increases count
        i = i + 1
    return count
