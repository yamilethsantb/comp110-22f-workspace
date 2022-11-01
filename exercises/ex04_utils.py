"""Excercise 4 - List Untility Functions."""
___author___ = "730361444"


def all(haystack: list[int], needle: int) -> bool:
    """Searches for given integer in list of intergers."""
    i: int = 0
    if len(haystack) == 0: 
        return False
    while i < len(haystack):
        if haystack[i] == needle:
            i += 1
        else:
            return False 
    return True


def max(the_input: list[int]) -> int: 
    """Searches for the max interger in a list of integers."""
    if len(the_input) == 0: 
        raise ValueError("max() arg is an empty list")
    i: int = 0 
    the_max: int = the_input[0]
    while i < len(the_input):
        if the_input[i] > the_max:
            the_max = the_input[i]
        i += 1
    return the_max


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Determines the deep equality of two lists of integers."""
    i: int = 0 
    r: int = 0
    the_first_sum: int = 0
    the_second_sum: int = 0 
    while i < len(first_list):
        the_first_sum += (first_list[i])
        i += 1
    while r < len(second_list):
        the_second_sum += (second_list[r])
        r += 1
    if the_first_sum == the_second_sum:
        return True 
    else: 
        return False 