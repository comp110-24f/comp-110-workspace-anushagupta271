from CQs.cq07.find_max import find_and_remove_max

"""Challenge Question 7 max_test"""

__author__ = "730646393"


def test_find_and_remove_max_use_case_1() -> None:
    """find_and_remove_max should return expected value."""
    assert find_and_remove_max([1, 2, 3]) == 3


def test_find_and_remove_max_use_case_2() -> None:
    """find_and_remove_max should return mutated list without the max."""
    test_list: list[int] = [3, 2, 3, 1]
    find_and_remove_max(test_list)
    assert test_list == [2, 1]


def test_find_and_remove_max_edge_case() -> None:
    """get_first called on an empty list should return ""."""
    assert find_and_remove_max([]) == -1
