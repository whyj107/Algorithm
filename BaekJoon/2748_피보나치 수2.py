import sys

# 재귀형식으로 풀 경우
# 반복 작업을 하기 때문에 느림
def fibo(n):
    return (n if n < 2 else fibo(n-1) + fibo(n-2))

if __name__=='__main__':
    # 빠르게 입력받기 위해서 int(input()) 대신 sys.stdin.readline()을 사용
    N = int(sys.stdin.readline())
    # 리스트 한개를 생성해서 0으로 초기화
    fibo_ = [0]*(N+1)
    # 피보나치 수열에서 1번째는 1이므로 1로 변경(인덱스가 0부터 시작한다고 가정)
    fibo_[1] = 1

    for i in range(2, N+1):
        # 문제에서 재시한 식을 이용
        fibo_[i] = fibo_[i-1] + fibo_[i-2]
    # 출력
    print(fibo_[-1])