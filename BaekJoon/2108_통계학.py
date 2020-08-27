import sys
from collections import Counter

n = int(sys.stdin.readline())

result = []
sum = 0

for i in range(n):
    i = int(sys.stdin.readline())
    result.append(i)
    sum += i

# 산술평균 출력(소수점 이하 첫째 자리에서 반올림)
print(round(sum/n))

# n이 1개일 경우 계산이 따로 필요 없음
if n == 1:
    # 중앙값 출력
    print(result[0])
    # 최빈값 출력
    print(result[0])
    # 범위 출력 = result[0] - result[0]
    print(0)
else:
    # 중앙값을 얻기 위해서 정렬
    result = sorted(result)
    # 중앙값 출력
    print(result[n//2])

    # 최빈값을 얻기 위해서 Counter를 이용
    # 빈도수를 dict로 만들어 줌
    cnt = Counter(result)
    # 배열 안에 튜플형식으로 최빈값부터 반환
    cnts = cnt.most_common()

    # 최빈값이 여러개일 경우 2번째 것 출력
    # 그래서 처음과 두번쨰만 비교한 후 두번째 것을 출력하면 됨
    if cnts[0][1] == cnts[1][1]:
        mode = cnts[1][0]
    else:
        mode = cnts[0][0]
    # 최빈값 출력
    print(mode)

    # 범위 출력
    print(result[-1]-result[0])