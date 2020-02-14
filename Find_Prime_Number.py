import math
# 에라토스테네스의 체 사용!
num_count = int(input())
num = list(map(int, input().split()))
# 문제가 1000이하의 자연수 이기 때문에
natural = list(range(2, 1001))
count = 0

if len(num) == num_count:
    for i in range(2, math.ceil(math.sqrt(1000))):
        for j in natural:
            # 자기 자신으로 나뉘는 것은 제외
            if j/i == 1:
                pass
            # 나누어 지는 수 존재 시 삭제
            elif j%i == 0:
                natural.remove(j)
for k in num:
    if k in natural:
        count += 1
print(count)