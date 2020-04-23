# 백준 10844 / 쉬운 계단 수
if __name__=='__main__':
    N = int(input())
    stair_nums = [[1 for _ in range(10)] for _ in range(101)]
    for i in range(2, N+1):
        for j in range(10):
            if 1 <= j <= 8:
                stair_nums[i][j] = stair_nums[i - 1][j - 1] + stair_nums[i - 1][j + 1]
            elif j == 0:
                stair_nums[i][j] = stair_nums[i - 1][j + 1]
            elif j == 9:
                stair_nums[i][j] = stair_nums[i - 1][j - 11]

    print(sum(stair_nums[N][1:10]) % 1000000000)