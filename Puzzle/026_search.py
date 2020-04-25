# 효율적인 입체 주차장

# 문제
# 10x10 주차장에서 왼쪽 위에서 오른쪽 아래로 이동하는 최소 횟수를 구해 보세요.

W, H = 10, 10
parking = [9] * (W + 1) + ([1] * W + [9]) * H + [9] * (W + 1)

goal = parking.copy()
goal[W + 1] = 2
start = parking.copy()
start[-W - 3] = 2

def search(prev, depth):
    target = []
    for parking, pos in prev:
        for d in [-1, 1, W + 1, - W - 1]:
            dd = pos + d
            if parking[dd] != 9:
                temp = parking.copy()
                temp[dd], temp[pos] = temp[pos], temp[dd]
                if str([temp, dd]) not in log:
                    target.append([temp, dd])
                    log[str([temp, dd])] = depth + 1
    temp = list(map(lambda x: str(x), target))
    if str([goal, (W + 1) * (H + 1) - 2]) in temp:
        return
    if len(target) > 0:
        search(target, depth + 1)

log = {}
log[str([start, (W + 1) * H - 2])] = 0
log[str([start, (W + 1) * (H + 1) - 3])] = 0
search([[start, (W + 1) * H - 2], [start, (W + 1) * (H + 1) - 3]], 0)
print(log[str([goal, (W + 1) * (H + 1) - 2])])