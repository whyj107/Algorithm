num = int(input())
tmp = 0

while num > 0:
    num -= tmp
    tmp += 1

num = tmp + num - 1
answer = str(num)+'/'+str(tmp-num)

# 짝수면 반대
if tmp % 2 == 0:
    answer = str(tmp-num)+'/'+str(num)
print(answer)