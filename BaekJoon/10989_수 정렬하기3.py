answer = []

# 카운팅 정렬(Counting Sort)
# 양의 정수로 된 배열에만 적용 가능
# 범용으로 사용하기 힘든 알고리즘
def counting_sort(arr):
    if min(arr) < 0:
        raise
    i, n, k = 0, len(arr), max(arr)+1
    c = [0]*k

    for j in range(n):
        c[arr[j]] = c[arr[j]] + 1
    for j in range(k):
        while c[j] > 0:
            (arr[i], c[j], i) = (j, c[j]-1, i+1)

for i in range(int(input())):
    n = int(input())
    answer.append(n)

counting_sort(answer)
# answer.sort()

for i in answer:
    print(i)
#---------------------------------------------------
import sys
series = [0] * 10001

for i in range(int(input())):
    a = int(sys.stdin.readline())
    series[a] = series[a] + 1

for b in range(len(series)):
    if series[b] !=0:
        for c in range(series[b]):
            print(b)