# 반복문을 사용하여 최대공약수 구하기
# 조건 01 : 2개의 수 a와 b에서 큰 수를 a라 하고, 작은 수를 b라고 했을 때
#           a%b가 0이 될 때까지 반복한다.

def gcd(p, q):
    if p > q:
        a = p
        b = q
    else:
        a = q
        b = p

    while b > 0:
        c = b
        b = a % b
        a = c
    return a

if __name__=='__main__':
    r = gcd(24, 64)
    print("24와 64의 최대공약수 : {0}".format(r))