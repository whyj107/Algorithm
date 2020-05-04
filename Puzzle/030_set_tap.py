# 멀티 탭으로 만든 문어 다리 배선

# 문제
# n=20일 때 몇 가지의 멀티 탭 배치를 생각할 수 있는지 구해 보세요
# (단, 전원 용량은 생각하지 않기로 한다.)

N = 20

def set_tap1(remain):
    if remain == 1:
        return 1
    cnt = 0
    # 2구
    for i in range(1, remain // 2 + 1):
        if remain - i == i:
            cnt += set_tap1(i) * (set_tap1(i) + 1) // 2
        else:
            cnt += set_tap1(remain - i) * set_tap1(i)
    # 3구
    for i in range(1, remain // 3 + 1):
        for j in range(i, (remain - i) // 2 + 1):
            if (remain - (i - j) == i) and (i == j):
                cnt += set_tap1(i) * (set_tap1(i) + 1) * (set_tap1(i) + 2) // 6
            elif remain - (i + j) == i:
                cnt += set_tap1(i) * (set_tap1(i) + 1) * set_tap1(j) // 2
            elif i == j:
                cnt += set_tap1(remain - (i + j)) * set_tap1(i) * (set_tap1(i) + 1) // 2
            elif remain - (i + j) == j:
                cnt += set_tap1(j) * (set_tap1(j) + 1) * set_tap1(i) // 2
            else:
                cnt += set_tap1(remain - (i + j)) * set_tap1(j) * set_tap1(i)
    return cnt

#print(set_tap1(N))

memo = {1: 1}
def set_tap2(remain):
    if remain in memo:
        return memo[remain]
    cnt = 0
    # 2구
    for i in range(1, remain // 2 + 1):
        if remain - i == i:
            cnt += set_tap2(i) * (set_tap2(i) + 1) // 2
        else:
            cnt += set_tap2(remain - i) * set_tap2(i)
    # 3구
    for i in range(1, remain // 3 + 1):
        for j in range(i, (remain - i) // 2 + 1):
            if (remain - (i + j) == i) and (i == j):
                cnt += set_tap2(i) * (set_tap2(i) + 1) * (set_tap2(i) + 2) // 6
            elif remain - (i + j) == i:
                cnt += set_tap2(i) * (set_tap2(i) + 1) * set_tap2(j) // 2
            elif i == j:
                cnt += set_tap2(remain - (i + j)) * set_tap2(i) * (set_tap2(i) + 1) // 2
            elif remain - (i + j) == j:
                cnt += set_tap2(j) * (set_tap2(j) + 1) * set_tap2(i) // 2
            else:
                cnt += set_tap2(remain - (i + j)) * set_tap2(j) * set_tap2(i)
    memo[remain] = cnt
    return cnt
print(set_tap2(N))
