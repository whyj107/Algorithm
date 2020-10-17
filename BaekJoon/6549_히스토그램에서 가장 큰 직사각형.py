# 히스토그램에서 가장 큰 직사각형
# https://www.acmicpc.net/problem/6549

# 다른 사람의 풀이
while True:
    n, *heights = list(map(int, input().split()))
    if (n == 0):
        break

    heights.insert(0, 0)

    heights += [0]
    checked = [0]
    area = 0

    for i in range(1, n + 2):
        while (checked and (heights[checked[-1]] > heights[i])):
            cur_height = checked.pop()
            area = max(area, (i - 1 - checked[-1]) * heights[cur_height])
        checked.append(i)
    print(area)

# 또 다른 사람의 코드
while True:
    N, *l=list(map(int, input().split()))
    l.append(0)
    if N == 0: break
    s=[]
    a=0
    for i,h in enumerate(l):
        while s and l[s[-1]]>h:
            ih=l[s.pop()]
            # s의 높이!
            w=i-s[-1]-1 if s else i
            # i에서부터 s의 top까지의 거리를 가로길이로 한다.
            # w = i일때는 마지막일 때
            if a<w*ih: a=w*ih
        s.append(i)
    print(a)