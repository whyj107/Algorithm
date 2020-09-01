# 문제
# 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

# 나의 풀이
import heapq
from collections import deque
def solution(operations):
    answer = []
    for i in operations:
        cmd, n = i.split()
        if cmd == 'I':
            heapq.heapify(answer)
            heapq.heappush(answer, (int(n)))
        elif cmd == 'D':
            try:
                answer = deque(answer)
                if n == '1': answer.pop()
                elif n == '-1': answer.popleft()
            except:
                pass
        answer = list(answer)
    return [max(answer), min(answer)] if not answer == [] else [0, 0]

# 다른 사람의 풀이
def solution1(operations):
    heap = []
    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
    if not heap:
        return [0, 0]
    return [max(heap), heap[0]]

if __name__ == '__main__':
    print(solution(["I 16", "D 1"]), [0, 0])
    print(solution(["I 7", "I 5", "I -5", "D -1"]), [7, 5])