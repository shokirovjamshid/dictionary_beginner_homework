def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    max_value = []
    for i in data:
        max_value.append(data[i])
    return max(max_value)

print(find_max_value(data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }))