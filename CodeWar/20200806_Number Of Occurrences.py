# 문제
# Number Of Occurrences
# https://www.codewars.com/kata/52829c5fe08baf7edc00122b/train/python

# 나의 풀이
def number_of_occurrences(element, sample):
    return sample.count(element)

if __name__ == '__main__':
    sample = [0, 1, 2, 2, 3]
    print(number_of_occurrences(0, sample), 1)
    print(number_of_occurrences(4, sample), 0)
    print(number_of_occurrences(2, sample), 2)
    print(number_of_occurrences(3, sample), 1)