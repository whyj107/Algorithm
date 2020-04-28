# 반복문(상향식 설계)을 사용하여 1부터 N까지의 합 구하기
# 조건 01 : table[n] = n + table[n-1](1<=n)

table = [0 for i in range(200)]

if __name__=='__main__':
    n = 100
    for i in range(n+1):
        if i == 1:
            table[i] = 1
        else:
            table[i] = table[i - 1] + i
    print("%d" % (table[n]))