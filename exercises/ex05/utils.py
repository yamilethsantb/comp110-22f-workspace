"""Skeleton code - EX05."""
__author__ = "730361444"


def only_evens(the_input: list[int]) -> list[int]:
    """Given a list...it returns even numbers."""
    the_return: list[int] = list()
    for num in the_input:
        if num % 2 == 0:
            the_return.append(num)
    return the_return


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Given two lists function will generate a new list that contains all elements."""
    the_return: list[int] = list()
    for num in first_list:
        the_return.append(num)
    for num in second_list:
        the_return.append(num)
    return the_return


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """The function should generate a List which is a subset of the given list given parameters!"""
    the_return: list[int] = list()
    if len(a_list) == 0:
        return the_return
    if len(a_list) == 1:
        return the_return
    if start_index == len(a_list):
        return the_return
    if start_index < 0: 
        i: int = 0
    else:
        i: int = start_index
    if end_index > len(a_list):
        end_index = (len(a_list))
    while i < end_index:
        the_return.append(a_list[i])
        i += 1
    return the_return