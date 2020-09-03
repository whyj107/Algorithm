# 문제
# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3

# 풀이
def solution(n, costs):
    answer = 0
    # 비용으로 정렬
    costs.sort(key=lambda x: x[2])
    visited = [0] * n
    visited[0] = 1
    while sum(visited) != n:
        for cost in costs:
            s, e, c = cost
            if visited[s] or visited[e]:
                if visited[s] and visited[e]:
                    continue
                else:
                    visited[s], visited[e] = 1, 1
                    answer += c
                    break
    return answer

# 크루스칼 알고리즘
def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer

if __name__ == '__main__':
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]), 4)