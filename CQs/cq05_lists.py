"""Mutating functions."""

__author__ = "730646393"


def manual_append(list: list[int], addition: int) -> None:
    list.append(addition)
    print(list)


def double(list: list[int]) -> None:
    i: int = 0
    while i < len(list):
        list[i] = list[i] * 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
