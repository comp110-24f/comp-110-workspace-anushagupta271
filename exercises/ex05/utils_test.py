from exercises.ex05.utils import only_evens, sub, add_at_index

"""Exercise 5 - utils_test"""

__author__ = "730646393"


# only_evens test cases
def test_only_evens_use_case_1() -> None:
    """only_evens should return expected list"""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_use_case_2() -> None:
    """only_evens should not mutate its input list"""
    list_1: list[int] = [1, 2, 3, 4]
    only_evens(list_1)
    assert list_1 == [1, 2, 3, 4]


def test_only_evens_edge_case() -> None:
    """only_evens should return empty string if no even numbers"""
    assert only_evens([1, 3]) == []


# sub test cases
def test_sub_use_case_1() -> None:
    """sub should return expected value"""
    assert sub([1, 2, 3, 4], 1, 3) == [2, 3]


def test_sub_use_case_2() -> None:
    """sub should not mutate its input list"""
    list_1: list[int] = [1, 2, 3, 4]
    sub(list_1, 1, 3)
    assert list_1 == [1, 2, 3, 4]


def test_sub_edge_case() -> None:
    """sub should return empty string input list is empty or start is greater than or equal to length of list or end is at most 0"""
    list_1: list[int] = [1]
    assert sub(list_1, 2, 4) == []


# add_at_index test cases
def test_add_at_index_use_case_1() -> None:
    """add_at_index should return expected value"""
    assert add_at_index([1, 2, 4, 5], 3, 2) == None


def test_add_at_index_use_case_2() -> None:
    """add-at_index should mutate its input list"""
    list_1: list[int] = [1, 2, 4, 5]
    add_at_index(list_1, 3, 2)
    assert list_1 == [1, 2, 3, 4, 5]


import pytest


def test_add_at_index_raise_indexerror() -> None:
    """add_at_index should raises Index Error if index is out of range"""
    with pytest.raises(IndexError):
        add_at_index([1], 3, 5)
