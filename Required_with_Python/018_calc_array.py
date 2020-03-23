# 배열 채우기(2)
# 조건 01 : 배열 a를 1부터 100까지 액세스할 때 a의 선은은 100 + 1개로 해야 한다.
# 조건 02 : 배열 a[0]의 초기값에 대해 고민해야 한다.

a = [0] * 101
def calc_array(n):
    a[1] = 1

    i = 2
    while i <= n:
        a[i] = a[i // 2] + 1
        i = i + 1

if __name__=='__main__':
    calc_array(100)
    i = 0
    while i <= 100:
        print(a[i])
        i = i + 1