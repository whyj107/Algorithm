# 합성 저항으로 만드는 황금비율

# 문제
# n=10일 때 조합하여 만들 수 있는 저항값 중 황금비율에 가장 가까운 값을 소수점 10자리까지 구해 보세요.

import itertools
from fractions import Fraction
tes = 0

def flatten_list(data):
    results = []
    for rec in data:
        if isinstance(rec, list):
           results.extend(rec)
           results = flatten_list(results)
        else:
            results.append(rec)
    return results

# 배열의 직적(Direct Product)을 계산
def product(ary):
    result = ary[0]
    for i in range(1, len(ary)):
        result = list(map(list, itertools.product(result, ary[i])))
    result = list(map(flatten_list, result))
    return result

# 병렬이면 저항값을 산출
def parallel(ary):
    temp = list(map(lambda x: Fraction(1.0/x), ary))
    return Fraction(1, sum(temp))

memo = {1: [1]}
def calc(n):
    if n in memo:
        return memo[n]
    # 직렬
    result = list(map(lambda x: x+1, calc(n - 1)))
    # 병렬
    for i in range(2, n + 1):
        # 병렬로 구분하는 개수를 설정
        cut = {}
        for ary in itertools.combinations(list(range(1, n)), i -1):
            pos = 0
            r = []
            
            for j in range(0, len(ary)):
                r.append(ary[j] - pos)
                pos = ary[j]
            r.append(n - pos)
            cut[str(sorted(r))] = list(sorted(r))
        # 구분할 위치에서 재귀적으로 저항을 설정
        for key, item in cut.items():
            temp = list(map(lambda x: calc(x), item))
            # 저항값을 계산
            for vv in product(temp):
                result.append(parallel(vv))
    memo[n] = result
    return result

golden_ratio = 1.61800339887
min_value = float("inf")
for i in calc(10):
    if abs(golden_ratio - i) < abs(golden_ratio - min_value):
        min_value = i
print("{:.10f}".format(float(min_value)))