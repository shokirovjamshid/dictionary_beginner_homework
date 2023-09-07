def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    keys_int_list = []
    for i in data:
        if str(i).isdigit():
            keys_int_list.append(i)
    return keys_int_list
print(find_int_keys(data = {
    'a': 1, 
    3 : 2, 
    'c': 3,
    10:'a'
  }))