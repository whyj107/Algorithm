# 문제
# 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3

# 풀이
def solution0(routes):
    answer = []
    routes.sort(key=lambda x: (x[0], x[1]))
    x, y = routes[0]
    for i in range(1, len(routes)):
        if routes[i][0] > y:
            answer.append(i)
            x, y = routes[i]
        else:
            y = min(routes[i][1], y)
    return len(answer) + (1 if answer[-1] != len(routes) else 0)

def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

if __name__ == '__main__':
    print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]), 2)