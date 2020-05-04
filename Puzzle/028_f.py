# 적절한 동아리 활동 배분

# 문제
# 클럽 부원 수는 최대 150명이며, 클럽 활동 시 필요한 운동장 면적을 최대로 하고자 한다.
# 그 면적의 최댓값을 구하라.

# 동적 계획법
club = [[11000, 40], [8000, 30], [400, 24], [800, 20], [900, 14],
        [1800, 16], [1000, 15], [7000, 40], [100, 10], [300, 12]]
N = 150

area = [None] * (len(club) + 1)

for i in range(0, len(area)):
    area[i] = [0] * (N + 1)

for i in range(len(club) - 1, -1, -1):
    for j in range(0, N + 1):
        if j < club[i][1]:
            area[i][j] = area[i + 1][j]
        else:
            area[i][j] = max(area[i + 1][j],
                             area[i+1][j-club[i][1]]+club[i][0])
print(area[0][N])

# 메모화
memo = {}
def search(club, remain):
    key = str([club, remain])
    if key in memo:
        return memo[key]
    max_value = 0
    for c in club:
        # 동아리를 추가하는 부원 수의 여유가 있는 경우
        if remain - c[1] >= 0:
            next_club = club.copy()
            next_club.remove(c)
            max_value = max([c[0] + search(next_club, remain - c[1]), max_value])
    memo[key] = max_value
    return max_value

print(search(club, 150))