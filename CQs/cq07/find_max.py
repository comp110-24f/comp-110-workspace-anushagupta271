"""Challenge question 7 find_max"""

__author__ = "730646393"


def find_and_remove_max(input: list[int]) -> int:
    if input == []:
        return -1
    else:
        i: int = 0
        max: int = -1
        while i < len(input):
            if max <= input[i]:
                max = input[i]
            i += 1
        i = 0
        while i < len(input):
            if max == input[i]:
                input.pop(i)
            else:
                i += 1
        return max
