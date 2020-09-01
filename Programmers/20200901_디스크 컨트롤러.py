# 문제
# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

# 풀이
import heapq
def solution(jobs):
    n = len(jobs)
    heap = []
    time, start = 0, -1
    cnt = 0
    answer = 0

    while cnt < n:
        for i in jobs:
            if start < i[0] <= time:
                answer += (time - i[0])
                heapq.heappush(heap, i[1])
        if len(heap) > 0:
            answer += len(heap)*heap[0]
            start = time
            time += heapq.heappop(heap)
            cnt += 1
        else:
            time += 1
    return answer//n

if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]), 9)