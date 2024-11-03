"""Exercise 5 - utils"""

__author__ = "730646393"


def only_evens(input: list[int]) -> list[int]:
    i: int = 0
    even_list: list[int] = []
    while i < len(input):
        if input[i] % 2 == 0:
            even_list.append(input[i])
        i += 1
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """sub generates a list which is a subset of the input list between the specified start index and end index"""
    sub_list: list[int] = []
    if len(input) == 0 or start >= len(input) or end <= 0:
        return sub_list
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)
    for i in range(start, end):
        sub_list.append(input[i])
    return sub_list


def add_at_index(input: list[int], element: int, index: int) -> None:
    """modify input list to place the lement at given index"""
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    ending: list[int] = sub(input, index, len(input))
    # print(ending)
    # print(input)
    # beginning: list[int] = sub(input, 0, index)
    if index == len(input):
        input.append(element)
    else:
        input[index] = element
    # print(input)
    # input.append(element)
    # print(input)
    if index < len(input):
        x: int = len(input) - 1
        # print(x)
        while x > index:
            input.pop(x)
            # print(input)
            # print(x)
            x = x - 1
            # print(x)
    i: int = 0
    while i < len(ending):
        input.append(ending[i])
        i += 1
    # print(input)
