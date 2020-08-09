# 문제
# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

# 나의 풀이
# 섞은 음식의 스코빌 지수
# = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수*2)
import heapq as hq
def solution(scoville, K):
    answer = 0
    heap = []
    for n in scoville:
        hq.heappush(heap, n)
    while heap[0] < K:
        try:
            hq.heappush(heap, hq.heappop(heap)+(hq.heappop(heap)*2))
        except IndexError:
            return -1
        answer += 1
    return answer

# 다른 사람의 풀이
def solution1(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7), 2)