def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    sum_float = 0
    for i in data:
        if int(data[i])!=data[i]:
            sum_float+=data[i]
    return sum_float

print(sum_float_values(data = {
    1: 22.4, 
    2: 3.5, 
    4: 1, 
    6: 7.6, 
    5: 2, 
    7: 3
  })) 