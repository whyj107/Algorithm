# 정수 삼각형
# 역순에서 계산해 나간다.

def solve(triangle):
    answer = [[] for _ in range(len(triangle))]
    # 삼각형을 뒤집어서 한 단계씩 내려간다.
    for i in range(len(triangle) - 1, - 1, - 1):
        # 어떤 단계인지에 따라서 나뉜다.
        for j in range(len(triangle[i])):
            # 맨 처음일 때는 각각을 answer 리스트에 넣어야 한다.
            if i == len(triangle) - 1:
                answer[i].append(triangle[i][j])
            # 맨 처음이 아닐 시 최대값을 골라서 넣는다.
            else:
                answer[i].append(triangle[i][j] + max(answer[i + 1][j], answer[i + 1][j + 1]))
    # 정답 출력
    print(answer)
    print(answer[0][0])

if __name__=='__main__':
    N = int(input())
    triangle = []
    for i in range(N):
        triangle.append(list(map(int, input().split())))

    solve(triangle)