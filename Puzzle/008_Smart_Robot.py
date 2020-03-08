# 똑똑한 로봇 청소기

# 문제
# 이 로봇이 12회 이동할 때, 생각할 수 있는 이동 경로의 패턴이 몇 가지인지 구해 보세요.

# 힌트
# 최초 3회까지는 진행 방향의 앞 방향과 좌우로 이동할 수 있지만, 4회째 이후부터는 움직일 수 없는 방향이 생긴다.

N = 12

def move(log):
    # 맨 처음의 위치를 포함하여 N+1개 조사하면 종료
    if len(log) == N + 1:
        return 1

    cnt = 0
    # 전후 좌우로 이동
    for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        # 탐색이 끝나지 않았으면 이동시킴
        next_pos = [log[-1][0] + d[0], log[-1][1] + d[1]]
        # 로그에 다음 위치가 기록되어 있는지 확인하기
        check = False
        for p in log:
            if p[0] == next_pos[0] and p[1] == next_pos[1]:
                # 있는 경우 플래그를 True로 변경
                check = True
        if check == False:
            cnt += move(log + [next_pos])
    return cnt

print(move([[0, 0]]))
