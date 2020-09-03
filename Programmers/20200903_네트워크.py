# 문제
# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

# 풀이
def solution(n, computer):
    answer = 0
    visited = [0]*n
    start = 0
    while 0 in visited:
        if visited[start] == 0:
            dfs(computer, visited, start)
            answer += 1
        start += 1
    return answer

def dfs(computer, visited, start):
    queue = [start]
    while queue:
        j = queue.pop()
        if visited[j] == 0:
            visited[j] = 1
        for i in range(0, len(computer)):
            if computer[j][i] == 1 and visited[i] == 0:
                queue.append(i)

if __name__ == '__main__':
    print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
    print(solution(4, [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]), 2)
    print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]), 1)