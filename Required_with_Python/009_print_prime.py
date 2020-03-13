# 2 ~ n 사이의 모든 소수를 추출하기
# 조건 01 : 2부터 N까지의 반복문으로 소수 확인 함수를 호출한다.

def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1

    if i == n:
        print("{0}는 소수".format(n))
    else:
        print("{0}는 합성수".format(n))

if __name__=='__main__':
    i = 2
    while i <= 20:
        check_prime(i)
        i = i + 1