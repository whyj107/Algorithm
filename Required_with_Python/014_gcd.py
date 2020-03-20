# 재귀 호출을 사용하여 최대공약수 구하기
# 조건 01 : 반복문의 코드 대신 재귀 호출로 작성한다.
# 조건 02 : 재귀 호출의 종료 조건은 작은 수가 0이 될 떄 종료한다.

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

if __name__=='__main__':
    r = gcd(24, 64)
    print("24와 64의 최대공약수 : {0}".format(r))