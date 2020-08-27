# 01 타일
# 피보나치와 비슷한 문제이다.

if __name__=='__main__':
    N = int(input())
    tile = [0] * (N + 1)
    tile[0] = 1
    tile[1] = 2

    for i in range(2, N):
        tile[i] = (tile[i-2] + tile[i-1]) % 15746

    print(tile[N-1])

    """
    # 이렇게 하면 메모리 초과가 나온다.
    for i in range(2, N):
        tile[i] = tile[i - 2] + tile[i - 1]
    print(tile[N - 1] % 15746)
    """