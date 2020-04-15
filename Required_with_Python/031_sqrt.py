# 제곱근 구하기
# 조건 01 : 어떤 정수 n의 제곱근을 구하기 위해서는 n에서 차례대로 1, 3, 5, 7, 9...를 빼서 다시 n에 저장한다.
#          n이 0보다 같거나 클 때까지 이 과정을 반복하고, n이 0보다 작아지면 지금까지 뺀 횟수가 n의 정수제곱근이 된다.

def f(n):
    a = [0] * 100
    i = 1
    while i <= n:
        a[i] = 0
        i += 1
    i = 1
    while i <= n:
        j = i
        while j <= n:
            a[j] = 1 - a[j]
            j += i
        i += 1
    cnt = 0
    i = 1
    while i <= n:
        if a[i] == 1:
            cnt += 1
        i += 1
    return cnt

if __name__=='__main__':
    print("10의 제곱근 : %d" % (f(10)))