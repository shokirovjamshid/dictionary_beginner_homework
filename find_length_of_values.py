def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    find_length_of_value = 0
    for i in data:
        find_length_of_value+=len(data[i])
    return find_length_of_value

print(find_length_of_values(data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }))