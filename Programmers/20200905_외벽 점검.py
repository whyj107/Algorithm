# 문제
# 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3

from collections import deque
import itertools
def next_index(queue, d, start=0):
    start_num = queue[start]
    for i in range(1, d+1):
        try:
            if queue[start+1] == start_num + i: start += 1
        except: break
    return start + 1

def solution(n, weak, dist):
    dist.sort(reverse=True)
    weak = deque(weak)
    for i in range(1, len(dist)+1):
        if i == 1:
            for _ in range(len(weak)):
                d = dist[0]
                if weak[-1] <= weak[0] + d: return 1
                else:
                    weak.append(weak.popleft()+n)
        else:
            dist2 = list(itertools.permutations(dist[:i]))
            for j in dist2:
                weak = deque(map(lambda x: x%n, weak))
                for _ in range(len(weak)):
                    start = 0
                    for d in j:
                        start = next_index(weak, d, start)
                        if start == len(weak): return i
                    weak.append(weak.popleft()+n)
    return -1

def solution1(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))

                if len(temp) == 0:
                    return (i + 1)
                elif temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))
    return -1

if __name__ == '__main__':
    print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]), 2)
    print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]), 1)