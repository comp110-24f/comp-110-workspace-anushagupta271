"""Exercise 3 - Utils"""

__author__ = "730646393"


def all(list: list[int], num: int) -> bool:
    """return true ohowr false to indicate whether or not all the numbers in the list are the num"""
    i: int = 0
    if len(list) == 0:
        return False
    else:
        while i < len(list):
            if len(list) == 0 or num != list[i]:
                return False
            else:
                i += 1
        return True


def max(list: list[int]) -> int:
    """return the largest number in the list"""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = list[0]
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if each index is equal to the same index of each list"""
    if len(list1) == 0 or len(list2) == 0 or len(list1) != len(list2):
        return False
    else:
        i: int = 0
        while i < len(list1):
            if list1[i] != list2[i]:
                return False
            i += 1
        return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Add list 2 to the end of list1 and return the mutated first list"""
    if len(list1) == 0 or len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1
    print(list1)
