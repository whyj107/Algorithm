# 알파벳 순서대로 하나씩 줄여가며 출력하기(재귀 호출 사용)
# 조건 01 : 반복문을 사용하여 'A'부터 문자를 출력한다.
# 조건 02 : 'Z'부터 하나씩 감소하여 재귀 함수를 호출한다.

def print_alphabet(end):
    if end < 'A' or end > 'Z':
        return -1
    c = ord('A')
    while c <= ord(end):
        print("%2c" % (c), end='')
        c += 1
    print()
    next = ord(end) - 1
    return print_alphabet(chr(next))

if __name__=='__main__':
    print_alphabet('Z')