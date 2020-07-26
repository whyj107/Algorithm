# 문제
# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3

# 나의 풀이
def solution(d, budget):
    answer = 0
    for i in sorted(d):
        if i <= budget:
            answer += 1
            budget -= i
    return answer

# 다른 사람의 풀이
def solution1(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

if __name__ == '__main__':
    print(solution([1, 3, 2, 5, 4], 9), 3)
    print(solution([2, 2, 3, 3], 10), 4)