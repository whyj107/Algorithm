# 조합 함수
from itertools import combinations

def solv(N, S, team):
    # 갭이 가장 작은 값을 찾기 위하여
    min_tmp = 99999

    for i in range(len(team) // 2):
        # start 팀
        team_start, start_sum = team[i], 0

        # link 팀
        team_link, link_sum = team[-i - 1], 0

        for j in range(N // 2):
            member_s = team_start[j]
            member_l = team_link[j]
            # start 팀
            for k in team_start:
                start_sum += S[member_s][k]
            # link 팀
            for k in team_link:
                link_sum += S[member_l][k]

        # 최솟값 찾기
        min_tmp = min(min_tmp, abs(start_sum - link_sum))

    return min_tmp


if __name__=='__main__':
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    members = [i for i in range(N)]
    team = []

    # 조합으로 가능한 팀 생성
    for x in list(combinations(members, N // 2)):
        team.append(x)

    answer = solv(N, S, team)
    print(answer)
