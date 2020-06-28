# 문제
# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

# 나의 풀이
def solution0(n, lost, reserve):
    lost_tmp = lost.copy()
    for i in lost:
        if i in reserve:
            lost_tmp.remove(i)
            reserve.remove(i)
    lost = lost_tmp.copy()
    for i in lost:
        if i-1 in reserve:
            lost_tmp.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            lost_tmp.remove(i)
            reserve.remove(i+1)
    return n - len(lost_tmp)

def solution(n, lost, reserve):
    # 체육복 여벌 가져온 사람이 도둑 맞은 경우 빌려줄 수 없기 때문에 소거 작업 진행
    l = list(set(lost) - set(reserve))
    r = list(set(reserve) - set(lost))

    # remove를 쓰기 위해서 lost_tmp 라는 list를 하나 더 만들어서 l을 copy한다.
    lost_tmp = l.copy()

    for i in l:
        if i-1 in r:
            lost_tmp.remove(i)
            r.remove(i-1)
        elif i+1 in r:
            lost_tmp.remove(i)
            r.remove(i+1)

    return n - len(lost_tmp)

# 다른 사람의 풀이
def solution1(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


if __name__ == '__main__':
    print(solution(5, [3], [2, 3]), 5)
    print(solution(3, [2], [2]), 3)
    print(solution(5, [3], [3, 4]), 5)
    print(solution(5, [2, 4], [1, 3, 5]), 5)
    print(solution(5, [2, 4], [3]), 4)
    print(solution(5, [2, 3], [3, 4]), 4)