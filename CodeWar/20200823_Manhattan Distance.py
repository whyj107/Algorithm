# 문제
# Manhattan Distance
# https://www.codewars.com/kata/52998bf8caa22d98b800003a/train/python

# 나의 풀이
def manhattan_distance(pointA, pointB):
    answer = 0
    for a, b in zip(pointA, pointB):
        answer += abs(a-b)
    return answer

# 다른 사람의 풀이
def manhattan_distance1(pointA, pointB):
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])

if __name__ == '__main__':
    print(manhattan_distance([1, 1], [1, 1]), 0)
    print(manhattan_distance([5, 4], [3, 2]), 4)
    print(manhattan_distance([1, 1], [0, 3]), 3)
