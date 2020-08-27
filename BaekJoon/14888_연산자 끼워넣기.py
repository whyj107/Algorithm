import sys

def Insert_Operator(now, level):
    if level == N:
        global min_n, max_n
        max_n = max(now, max_n)
        min_n = min(now, min_n)
        return

    # 더하기
    if oper[0] > 0:
        oper[0] -= 1
        Insert_Operator(now + num[level], level+1)
        oper[0] += 1

    # 빼기
    if oper[1] > 0:
        oper[1] -= 1
        Insert_Operator(now - num[level], level+1)
        oper[1] += 1

    # 곱하기
    if oper[2] > 0:
        oper[2] -= 1
        Insert_Operator(now * num[level], level+1)
        oper[2] += 1

    # 나누기
    if oper[3] > 0:
        tmp = abs(now) // num[level]
        # 음수일 경우 확인
        if now < 0:
            tmp *= -1
        oper[3] -= 1
        Insert_Operator(tmp, level+1)
        oper[3] += 1

if __name__=='__main__':
    # 수의 개수
    N = int(sys.stdin.readline())
    # 숫자들
    num = list(map(int, sys.stdin.readline().split()))
    # 덧셈 수, 뺄셈 수, 곱셈 수, 나눗셈 수
    oper = list(map(int, sys.stdin.readline().split()))

    # 출력 관련 범위
    min_n = 10 ** 9
    max_n = -10 ** 9

    now = num[0]

    Insert_Operator(now, 1)

    print(max_n)
    print(min_n)
    #sys.stdout.write(str(max_n) + '\n' + str(min_n))