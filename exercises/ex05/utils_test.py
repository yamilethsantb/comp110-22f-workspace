"""Tests for utils functions."""
__author__ = "730361444"


from utils import only_evens 
from utils import concat 
from utils import sub


def test_only_evens_empty() -> None:
    """Test when list is empty."""
    assert only_evens([]) == list()


def test_only_evens_all_evens() -> None:
    """When all numbers are even."""
    assert only_evens([3, 4, 9, 10]) == [4, 10]


def test_only_evens_one_even() -> None:
    """When there is only one even in the list."""
    assert only_evens([1, 3, 5, 8]) == [8]


def test_concat_two_empty_list() -> None:
    """When both lists are empty."""
    assert concat([], []) == list()


def test_concat_identical_lists() -> None:
    """When both tests are identical."""
    assert concat([3, 4], [3, 4]) == [3, 4, 3, 4]


def test_concat_diff_values() -> None:
    """Test when lists are of different values."""
    first_list: list[int] = [3, 4]
    second_list: list[int] = [8, 10, 3]
    assert concat(first_list, second_list) == [3, 4, 8, 10, 3]


def sub_empty_list() -> None:
    """When list is empty should return empty list."""
    assert sub([], 3, 5) == list()


def sub_start_index_is_zero() -> None:
    """When start value is equal to zero."""
    assert sub([4, 5, 6, 7], 0, 3) == [4, 5, 6]


def sub_end_index_is_greater_than_length() -> None:
    """When last index is greater than the length of the list."""
    assert sub([4, 5, 6, 7], 0, 7) == [4, 5, 6, 7]