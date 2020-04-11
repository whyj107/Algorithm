# 등수 구하기
# 조건 01 : 전체 점수의 처음부터 끝까지 반복하여 현재의 점수가 몇 번째의 크기를 갖는지를 계산한다.

MAX = 30
a = [75, 25, 6, 73, 43, 46, 31, 13, 60, 90,
     5, 43, 35, 65, 100, 28, 83, 95, 35, 45, -1]

rank = [0] * MAX

i = 0
while a[i] != -1:
    rank[i] = 1
    j = 0
    while a[j] != -1:
        if a[j] > a[i]:
            rank[j] = rank[i] + 1
        j = j + 1
    i = i + 1
for i in range(len(a)):
    print('%6d 점 - : %6d 등'%(a[i], rank[i]))