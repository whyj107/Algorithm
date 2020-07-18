# 문제
# 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

# 나의 풀이
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return -1

# 다른 사람의 풀이
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]

if __name__ == '__main__':
    print(solution([4, 3, 2, 1]), [4, 3, 2])
    print(solution([10]), -1)