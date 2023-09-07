def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    max_key = []
    for i in data:
        max_key.append(i)
    return max(max_key)

print(find_max_key(data = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  }))