"""Dictionary related utility functions."""

__author__ = "730361444"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list(str) of all values in a single column."""
    result: list[str] = []
    for row in rows:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], number_row: int) -> dict[str, list[str]]:
    """Produce a new column based table with only a given amount of rows of data."""
    result: dict[str, list[str]] = {}
    if number_row >= len(table): 
        return table
    for key in table.keys():
        value = table[key]
        result_2: list[str] = []
        for i in range(number_row):
            result_2.append(value[i])
        result[key] = result_2
    return result
        

def select(data: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Allows to select columns we care about."""
    result: dict[str, list[str]] = {}
    for column in columns: 
        result[column] = data[column]
    return result


def concat(first_list: dict[str, list[str]], second_list: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in first_list:
        result[column] = first_list[column]
    for other in second_list:
        if other in result:
            result[other] += second_list[other]
        else:
            result[other] = second_list[other]
    return result 


def count(count: list[str]) -> dict[str, int]: 
    """Counting the number of times the value appears in input list."""
    empty_dict: dict[str, int] = {}
    for i in count:
        if i in empty_dict:
            empty_dict[i] += 1
        else: 
            empty_dict[i] = 1
    return empty_dict