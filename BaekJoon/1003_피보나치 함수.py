cnt0 = 0
cnt1 = 0
# 문제에서 나온 함수
def fibonacci(N):
    global cnt0, cnt1
    if N == 0:
        cnt0 += 1
        return 0
    elif N == 1:
        cnt1 += 1
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)

if __name__=='__main__':
    # T 입력 받기
    T = int(input())

    # N의 범위가 40 이하
    # N이 0일 때 (0의 개수, 1의개수) == [1, 0]
    fibo_ = [[1, 0]]*(41)
    fibo_[1] = [0, 1]

    for i in range(T):
        # N 입력 받기(0<= N <=40)
        N = int(input())

        # 함수 실행(이 방법으로 하면 느리다)
        # fibonacci(N)

        # 정답 출력
        # print(cnt0, cnt1)

        # cnt0과 cnt1 초기화
        # cnt0 = 0
        # cnt1 = 0

        for j in range(2, N + 1):
            fibo_[j] = [fibo_[j-1][0]+fibo_[j-2][0], fibo_[j-1][1]+fibo_[j-2][1]]

        print(fibo_[N][0], fibo_[N][1])