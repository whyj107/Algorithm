# 배열 채우기(1)
# 조건 01 : 배열을 사용할 때 인덱스 + 1 개의 배열을 선언해야 한다.
# 조건 02 : 이전 2개의 항목을 더하여 현재 배열의 값으로 저장한다.

a = [1] * 100
def calc_array(n):
    a[1] = 1
    a[2] = 1

    i = 3
    while i <= n:
        a[i] = a[i-1] + a[i-2] + 1
        i = i + 1

if __name__=='__main__':
    calc_array(10)
    i = 0
    while i <= 7:
        print(a[i])
        i = i + 1
