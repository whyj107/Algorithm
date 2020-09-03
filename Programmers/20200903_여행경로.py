# 문제
# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3

# 풀이
def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for s, e in tickets:
        if s in routes:
            routes[s].append(e)
        else:
            routes[s] = [e]
    queue = ['ICN']
    answer = []
    while queue:
        n = queue[-1]
        if n not in routes or len(routes[n]) == 0:
            answer.append(queue.pop())
        else:
            queue.append(routes[n].pop())
    return list(reversed(answer))

if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]),
          ["ICN", "JFK", "HND", "IAD"])
    print(solution([["ICN", "SFO"], ["ICN", "ATL"],
                    ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]),
          ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])