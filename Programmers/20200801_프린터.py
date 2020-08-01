# 문제
# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

# 풀이
def solution0(priorities, location):
    answer = 0
    while len(priorities) != 0:
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location = len(priorities)-1

            else:
                return answer+1
        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location -= 1
            else:
                priorities.pop(0)
                location -= 1
                answer += 1

def solution1(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2), 1)
    print(solution([1, 1, 9, 1, 1, 1], 0), 5)