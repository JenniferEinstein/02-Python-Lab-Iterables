# Exercise 1: Create a set from a list, removing duplicates.
def create_set(lst):
    thisSet = {lst}
    print(thisSet)
    pass

# Exercise 2: Find the union of two sets.
def union_sets(set1, set2):
    print(set1 | set2)
    pass

# Exercise 3: Find the intersection of two sets.
def intersection_sets(set1, set2):
    print(set1 & set2)
    pass

# Exercise 4: Check if one set is a subset of another.
def is_subset(set1, set2):
    answer=set2.issubset(set1) or set1.issubset(set2)
    print(answer)
    return answer
    pass

# Exercise 5: Find the symmetric difference of two sets.
def symmetric_difference_sets(set1, set2):
    print(set1^set2)
    pass
