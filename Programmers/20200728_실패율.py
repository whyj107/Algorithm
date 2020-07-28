# 문제
# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

# 나의 풀이
def solution(N, stages):
    tmp = {i: 0.0 for i in range(1, N+1)}
    pre_cnt = 0
    for i in range(1, N+1):
        if stages.count(i) != 0:
            tmp[i] = stages.count(i)/(len(stages)-pre_cnt)
        pre_cnt += stages.count(i)
    return sorted(tmp, key=lambda x: tmp[x], reverse=True)

# 다른 사람의 풀이
def solution1(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5])
    print(solution(8, [1, 2, 3, 4, 5, 6, 7]), [7, 6, 5, 4, 3, 2, 1, 8])