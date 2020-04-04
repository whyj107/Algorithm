# 30인 31각에 도전!

# 문제
# 30인을 한 줄로 세우는 경우 몇 가지 방법이 있는지 구해 보세요.
# 남녀의 배열 방법만 생각하는 것으로 하고, 누가 어느 위치에 서는지는 무시하기로 합니다.
# 예를 들어 4인(4인 5각)의 경우 8가지가 있다.

# 남자와 여자를 문자로 설정
boy, girl = "B", "G"
N = 30

# 재귀 방법
def add(seq):
    # 나열할 사람 수에 도달하면 종료
    if len(seq) == N:
        return 1
    # 30명 미만인 경우 남자를 추가하거나 오르쪽 끝이 남자인 경우 여자를 추가
    cnt = add(seq + boy)
    if seq[-1] == boy:
        cnt += add(seq + girl)
    return cnt

# 남자와 여자에서 개시하여 카운트
print(add(boy) + add(girl))

# ----------------------------------------------------

N = 30
boy, girl = 1, 0
for i in range(0, N):
    # n-1명까지 늘어서 있는 상태에서 구한다
    boy, girl = boy + girl, boy
print(boy + girl)