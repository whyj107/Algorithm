# 우회전을 못해도 괜찮다고?

# 문제
# 6블록 x 4블록이라면 몇 가지 길이 있는지 구해보세요.

W, H = 6, 4
# 이동 방향
DIR = [[0, 1], [-1, 0], [0, -1], [1, 0]]
# 세로 선을 사용했는지 비트 단위로 저장
left = [0] * H
# 가로 선을 사용했는지 비트 단위로 저장
bottom = [0] * W

def search(x, y, dir, left, bottom):
    left_l = left.copy()
    bottom_l = bottom.copy()
    # 경계를 넘거나 사용 완료된 경우는 진행할 수 없음
    if (dir == 0) or (dir == 2):
        # 상하로 이동한 경우
        pos = min([y, y + DIR[dir][1]])
        if (pos < 0) or (y + DIR[dir][1] > H):
            return 0
        if left_l[pos] & (1 << x) > 0:
            return 0
        # 세로 선을 사용 완료로 함
        left_l[pos] |= (1 << x)
    else:
        pos = min([x, x + DIR[dir][0]])
        if (pos < 0) or (x + DIR[dir][0] > W):
            return 0
        if bottom_l[pos] & (1 << y) > 0:
            return 0
        # 가로 선을 사용 완료로 함
        bottom_l[pos] |= (1 << y)
    next_x, next_y = x + DIR[dir][0], y + DIR[dir][1]
    if (next_x == W) and (next_y == H):
        # B에 도달하면 종료
        return 1

    cnt = 0
    # 직진
    cnt += search(next_x, next_y, dir, left_l, bottom_l)
    # 좌회전
    dir = (dir + 1) % len(DIR)
    cnt += search(next_x, next_y, dir, left_l, bottom_l)
    return cnt

# 시작점으로부터 오른쪽으로 시작
print(search(0, 0, 3, left, bottom))