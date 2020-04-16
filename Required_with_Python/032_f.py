# 알파벳 순서대로 하나씩 줄여가며 출력하기(반복문 사용)
# 조건 01 : 26행을 반복하여 출력한다.
# 'A'부터 ('Z' - 'A')만큼 출력한다.

def f():
    a = ord('A')
    while a <= ord('Z'):
        b = ord('A')
        while b <= (ord('Z') - (a - 65)):
            print('%2c'%(b), end = "")
            b += 1
        print()
        a += 1

if __name__=='__main__':
    f()