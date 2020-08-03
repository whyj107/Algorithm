# 문제
# Number Zoo Patrol
# https://www.codewars.com/kata/5276c18121e20900c0000235/train/python

# 나의 풀이
def find_missing_number(numbers):
    if len(numbers) < 1:
        return 1
    num = (1+max(numbers))*(len(numbers)+1)*0.5-sum(numbers)
    return int(num*2) if int(num) in numbers or int(num) != num else int(num)

# 다른 사람의 풀이
def find_missing_number1(a):
    n = len(a) + 1
    return n * (n + 1) // 2 - sum(a)

if __name__ == '__main__':
    print(find_missing_number([2, 3, 4]), 1)
    print(find_missing_number([1, 3, 4]), 2)
    print(find_missing_number([1, 2, 4]), 3)
    print(find_missing_number([1, 2, 3]), 4)