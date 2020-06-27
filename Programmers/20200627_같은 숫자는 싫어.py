# 문제
# 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

# 나의 코드
def solution(arr):
    pre = arr[0]
    answer = [pre]
    for i in arr:
        if i != pre:
            answer.append(i)
        pre = i
    return answer

# 다른 사람의 코드
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

if __name__ == '__main__':
    print(solution([1, 1, 3, 3, 0, 1, 1]), [1, 3, 0, 1])
    print(solution([4, 4, 4, 3, 3]), [4, 3])