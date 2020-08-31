# 문제
# LCS
# https://www.acmicpc.net/problem/9251

# 풀이
A = list(str(input()))
B = list(str(input()))
lcs = [[0]*(len(A)+1) for _ in range(len(B)+1)]
answer = 0
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            lcs[j+1][i+1] = lcs[j][i] + 1
            answer = max(answer, lcs[j+1][i+1])
        else:
            lcs[j+1][i+1] = max(lcs[j][i+1], lcs[j+1][i])
print(answer)