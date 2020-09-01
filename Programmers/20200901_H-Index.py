# 문제
# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

# 나의 풀이
# 런타임 오류와 에러가 난다. -> 문제를 잘못이해했다.
def solution0(citations):
    return max([i for idx, i in enumerate(sorted(citations)) if(idx+1) >= i ])

def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i:
            return len(citations)-i
    return 0

if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]), 3)