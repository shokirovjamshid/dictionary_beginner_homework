def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    age_list = []
    name_list = []
    for i in data:
        age_list.append(i['age'])
        name_list.append(i['name'])
    max_age = max(age_list)
    max_name = name_list[age_list.index(max_age)]
    return max_name

print(get_max_age_user_name(data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  }, 
  {
    'name': 'Ban', 
    'age': 29
  }
]))