# 문제
# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3

def check(answer):
    for x, y, a in answer:
        # 기둥
        if a == 0:
            # 바닥 위, 보의 한쪽 끝 부분(x-1, x), 다른 기둥 위
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer: continue
            else: return False
        # 보
        elif a == 1:
            # 보 아래 끝에 기둥, 양족 끝 부분 다른 보 연결
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer): continue
            else: return False
    return True


def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, a, b = i
        if b == 1:
            answer.append([x, y, a])
            if not check(answer): answer.remove([x, y, a])
        elif b == 0:
            answer.remove([x, y, a])
            if not check(answer): answer.append([x, y, a])
    answer.sort()
    return answer

if __name__ == '__main__':
    print(solution(	 5, [[1, 0, 0, 1], [1, 1, 1, 1],
                        [2, 1, 0, 1], [2, 2, 1, 1],
                        [5, 0, 0, 1], [5, 1, 0, 1],
                        [4, 2, 1, 1], [3, 2, 1, 1]])==
          [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1],
           [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]])