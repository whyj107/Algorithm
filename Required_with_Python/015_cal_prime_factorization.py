# 소인수 분해 구하기
# 조건 01 : 주어진 숫자 n이 i로 나누어지면 해당 i는 n의 인수에 해당하며 n = n/i로 저장하여 이 과정을 반복한다.
# 조건 02 : 반복문을 간단하게 하기 위해 무한루프를 사용한다.

def calc_prime_factorization(n):
    i = 2
    while i <= n:
        while 1:
            if n % i == 0:
                print(i, end=" ")
                n = n // i
            else:
                break
        i = i + 1

if __name__=='__main__':
    calc_prime_factorization(48)
