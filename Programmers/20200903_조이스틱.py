# 문제
# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

# 풀이
def solution(name):
    cnt = 0
    a_cnt = 0
    a_max = 0
    a_idx = 0

    for i, n in enumerate(name):
        if n == 'A':
            a_cnt += 1
            if a_cnt > a_max:
                a_max = a_cnt
                a_idx = i
        else:
            cnt += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
            a_cnt = 0

    a_startIdx = a_idx - a_max + 1

    if a_startIdx == 0 or a_idx == len(name) - 1:
        cnt += len(name) - 1 - a_max
    else:
        left = len(name) - a_idx - 1
        if a_startIdx <= left:
            wander_cnt = (a_startIdx-1) * 2 + left
        else:
            wander_cnt = a_startIdx + left * 2
        cnt += min(wander_cnt, len(name) - 1)
    return cnt

if __name__ == '__main__':
    print(solution("JAZ"), 11)
    print(solution("BBBAAAB"), 9)
    print(solution("ABABAAAAABA"), 11)