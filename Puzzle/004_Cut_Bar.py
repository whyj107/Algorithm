# 길이 n[cm]의 한 막대를 1[cm] 단위로 자른다고 생각해 봅시다.
# 단, 하나의 막대는 한 번에 한 사람만이 자를 수 있습니다.
# 잘린 막대가 3개가 되면, 동시에 3명이 자를 수 있습니다.
# 최대 m명이 있을 때 막대를 자르는 최소 횟수를 구해 보세요.

# n=20, m=3일 때의 횟수를 구해보세요.
# n=100, m=5일 때의 횟수를 구해보세요.

# current는 현재 막대의 개수
def cutbar(m, n, current):
    if current >= n:
        # 잘라내기 끝
        return 0
    elif current < m:
        # 다음은 현재의 2배가 된다.
        return 1 + cutbar(m, n, current*2)
    else:
        # 가위 수 만큼 추가
        return 1 + cutbar(m , n, current+m)

print(cutbar(3, 20, 1))
print(cutbar(5, 100, 1))

# -----------------------

def cutbar(m, n):
    count = 0
    current = 1
    while n > current:
        current += current if current < m else m
        count += 1
    print(count)

cutbar(3, 20)
cutbar( 5, 100)
