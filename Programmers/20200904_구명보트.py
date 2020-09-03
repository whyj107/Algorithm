# 문제
# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

# 풀이
def solution(people, limit):
    people.sort()
    cnt = 0
    i, j = 0, len(people) - 1
    while i <= j:
        cnt += 1
        if people[i]+people[j] <= limit:
            i += 1
        j -= 1
    return cnt

if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100), 3)
    print(solution([70, 80, 50], 100), 3)