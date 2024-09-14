# Exercise 1: Create a dictionary from two lists (keys and values).
def create_dict(keys, values):
    thisDictionary = zip(keys, values)
    print(thisDictionary)
    return thisDictionary
    pass


# Exercise 2: Merge two dictionaries.
def merge_dicts(dict1, dict2):
    married_dicts = dict1 | dict2
    print(married_dicts)
    return married_dicts
    pass

# Exercise 3: Find the key of the maximum value in a dictionary.
def max_value_key(d):
    maxKey = max(d, key=d.get)
    print(maxKey)
    return maxKey
    pass

    # maxKey = max(zip(d.values(), d.keys())),[1]
    # print(maxKey)
    # return(maxKey)
    # pass

# Exercise 4: Sort a dictionary by values.
def sort_dict_by_value(d):
    pass

# Exercise 5: Count the occurrences of elements in a list using a dictionary.
def count_elements(lst):
    pass
