# 문제
# JavaScript Array Filter
# In Python, there is a built-in filter function that operates similarly to JS's filter.
# For more information on how to use this function, visit https://docs.python.org/3/library/functions.html#filter
#
# The solution would work like the following:
# get_even_numbers([2,4,5,6]) => [2,4,6]

# My Code
def get_even_numbers(arr):
    return [i for i in arr if i % 2 == 0]

def get_even_numbers1(arr):
    return list(filter(lambda x: x % 2 == 0, arr))

if __name__=='__main__':
    print(get_even_numbers([2,4,5,6]))