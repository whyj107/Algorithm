# 문제
# 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3

# 나의 문제 풀이
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]

if __name__ == '__main__':
    print(solution([5, 9, 7, 10], 5), [5, 10])
    print(solution([2, 36, 1, 3], 1), [1, 2, 3, 36])
    print(solution([3, 2, 6], 10), [-1])