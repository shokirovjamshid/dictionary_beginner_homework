def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    name_list = []
    for i in data:
        if min_age<=i['age'] and max_age>=i['age']:
            name_list.append(i['name'])
    return name_list

print(get_user_names_with_age_range( data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
]
,min_age = 18
,max_age = 25))