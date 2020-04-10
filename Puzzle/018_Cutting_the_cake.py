# 케이크 자르기

# 문제
# 이웃한 두 개의 케이크에 올려져 있는 딸기 수의 합이 모두 제곱수가 되도록 잘라야만 한다.
# 이 조건을 만족하는 방법으로 자를 수 있는 최소의 N(>1)을 구해보세요.

from math import sqrt, floor

def check(last_n, used, ary):
    # 모두 사용 완료이며 맨 앞의 '1'과 제곱수가 되면 종료
    if (False not in used) and (last_n in ary[1]):
        return [1]
    # 후보를 순서대로 시험한다.
    for i in ary[last_n]:
        # 사용 완료가 아닌 경우
        if (len(used) > i - 1) and (used[i - 1] == False):
            used[i - 1] = True
            result = check(i, used, ary)
            # 발견한 경우 그 값을 추가하여 돌려줌
            if len(result) > 0:
                return [i] + result
            used[i - 1] = False
    return []

n = 2
result = []
while True:
    square = map(lambda x: x ** 2, range(2, floor(sqrt(n * 2)) + 1))
    square = list(square)
    # 이웃할 가능성이 있는 후보를 작성
    ary = {}
    for i in range(1, n + 1):
        temp = map(lambda x: x - i, square)
        temp = filter(lambda x: x > 0, temp)
        ary[i] = list(temp)
    # '1'을 사용 완료로 하고, '1'부터 탐색 개시
    result = check(1, [True] + [False] * (n - 1), ary)
    if len(result) > 0:
        break
    n += 1
print(n)
print(result)