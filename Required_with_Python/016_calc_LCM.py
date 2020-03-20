# 최소공배수 구하기
# 조건 01 : 반복문을 사용하여 2개의 숫자가 모두 나눠질 수 있는 첫 번째 나오는 수를 구한다.
# 조건 02 : 반복문의 끝을 어떤 수로 설정할지 고민해야 한다.

def calc_LCM(n):
    a = 2
    b = 3
    c = 5
    i = 2

    while i < n:
        if (i % a == 0) and (i % b == 0) and (i % c == 0):
            break
        i = i + 1

    print("2, 3, 5의 최소공배수 : {0}".format(i))

if __name__=='__main__':
    calc_LCM(100)