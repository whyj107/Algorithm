# 문제
# 풍선 터트리기
# https://programmers.co.kr/learn/courses/30/lessons/68646?language=python3

# 시간 초과...
def solution1(a):
    answer = 0
    premin, sufmin = float('inf'), float('inf')
    for idx, i in enumerate(a):
        if idx != 0:
            premin = min(a[:idx])
        if idx != len(a)-1:
            sufmin = min(a[idx+1:])
        if premin > i or sufmin > i:
            answer += 1
    return answer

def solution(a):
    tmp = [False]*len(a)
    premin, sufmin = float('inf'), float('inf')
    for i in range(len(a)):
        if premin > a[i]:
            tmp[i] = True
        if premin > a[i]:
            premin = a[i]
    for i in range(len(a)-1, -1, -1):
        if sufmin > a[i]:
            tmp[i] = True
        if sufmin > a[i]:
            sufmin = a[i]
    return tmp.count(True)

print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))