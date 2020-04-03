# 끈 세 개로 만드는 사각형

# 문제
# 끈의 길이를 1부터 500까지 변화시킨다고 할 때
# 두 개의 직사각형의 면적의 합과 정사각형의 면적이 같아지는 조합이 몇 가지 있는지 구해 보세요.

from itertools import combinations
from math import gcd

MAX = 500
cnt = 0

# 정사각형
for c in range(1, MAX // 4 + 1):
    # 정사각형 한 변
    for a, b in combinations(range(1, c), 2):
        if a * a + b * b == c * c:
            if gcd(a, b) == 1:
                cnt += 1

print(cnt)