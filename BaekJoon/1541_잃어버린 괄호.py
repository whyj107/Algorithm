# 문제
# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

# 나의 풀이
answer = 0
sik = input().split('-')
for i in sik[0].split('+'):
    answer += int(i)
for i in sik[1:]:
    for j in i.split('+'):
        answer -= int(j)
print(answer)