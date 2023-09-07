def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    age_list = []
    name_list = []
    for i in data:
        age_list.append(i['age'])
        name_list.append(i['name'])
    min_age = min(age_list)
    min_name = name_list[age_list.index(min_age)]
    return min_name

print(get_min_age_user_name(data = [
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