import sys
import math
# 10000 이하의 모든 소수 생성
N = 10000 + 1
is_prime = [True]*N
for i in range(2, math.ceil(math.sqrt(N))):
    if is_prime[i]:
        for j in range(2*i, N, i):
            is_prime[j] = False
prime_list = [i for i, j in enumerate(is_prime) if j == True and i >= 2]

gold = [[] for _ in range(N)]

for i in range(len(prime_list)):
    for j in range(i, len(prime_list)):
        # 두 소수의 값이 짝수인지 판별
        even = prime_list[i] + prime_list[j]
        if even % 2 == 0 and even <= 10000:
            gold[even].append([prime_list[i], prime_list[j]])

for _ in range(int(sys.stdin.readline())):
    num = int(input())
    answer = [0, 0]
    # 두수의 차이가 작은 수 = 곱이 가장 큰 수
    for [i, j] in gold[num]:
        if i*j > answer[0] * answer[1]:
            answer[0] = i
            answer[1] = j
    print(answer[0], answer[1])