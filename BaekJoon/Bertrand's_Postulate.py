# 에라토스테네스의 체를 이용하여 소수 구하고
# 맞는 소수 출력

import sys
import math
# 소수리스트 만들기
# 문제 범위 : 123456의 2배
N = 123456 * 2 + 1
is_prime = [True] * N
prime_list = []

for i in range(2, math.ceil(math.sqrt(N))):
    # True일 경우 소수
    if is_prime[i]:
        # 배수 : False
        for j in range(2*i, N, i):
            is_prime[j] = False

# 소수 출력
num = int(sys.stdin.readline())
while num != 0:
    answer = 0
    # n 보다 크고 2n 보다 작은 수 사이 소수 갯수
    for i in range(num+1, num*2+1):
        if is_prime[i]:
            answer += 1
    print(answer)
    num = int(sys.stdin.readline())