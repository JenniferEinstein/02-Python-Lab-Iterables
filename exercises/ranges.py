# Exercise 1: Create a list of numbers using range().
def create_range(start, end, step=1):
    answer = range(start, end, step)
    print(answer)
    return answer
    

# Exercise 2: Sum all elements in a range.
def sum_range(start, end):
    result = sum(range(start, end+1))
    print(result)
    return(result)
    

# Exercise 3: Check if a number is within a range.
def in_range(n, start, end):
    for i in range(start, end):
        if i == n:
            print(True)
            return True
    print(False)
    return(False)
    pass

# Exercise 4: Create a list of even numbers using range().
def even_numbers(start, end):
    if start % 2 != 0:
        start += 1
    even_list = list(range(start, end, 2))
    print(even_list)
    return even_list
    

# Exercise 5: Iterate over a range in reverse.
def reverse_range(start, end):
    pass
