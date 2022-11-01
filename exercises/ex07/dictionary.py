"""Dictionary Functions - ex07."""
___author___ = "730361444"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the given dictionary."""
    result: dict[str, str] = {}
    for key in x:
        value = x[key]
        result[value] = key
    if len(result) != len(x):
        raise KeyError("KeyError")
    return result


def invert_3(x: dict[str, int]) -> dict[int, str]:
    """Also invert the given given dictionary."""
    result: dict[int, str] = {}
    for key in x:
        value = x[key]
        result[value] = key
    return result


def favorite_color(x: dict[str, str]) -> str:
    """From a data set returns the favorite color out of the group."""
    result: list[str] = list()
    for key in x:
        value = x[key]
        result.append(value)
    new_dict = count(result)
    new_result: list[int] = list()
    for frequency in new_dict:
        value_2 = new_dict[frequency]
        new_result.append(value_2)
    z: int = 0 
    the_max: int = new_result[0]
    while z < len(new_result):
        if new_result[z] > the_max:
            the_max = new_result[z]
        z += 1
    new_dict = invert_3(new_dict)
    needed_value = new_dict[the_max]
    return (needed_value)


def count(x: list[str]) -> dict[str, int]:
    """Counts the frequency of each string value in the list and produces a dictionary."""
    empty_dict: dict[str, int] = {}
    for i in x:
        if i in empty_dict:
            empty_dict[i] += 1
        else: 
            empty_dict[i] = 1
    return empty_dict