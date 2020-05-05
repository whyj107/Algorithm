# 문제
# Get ASCII value of a character.
# For the ASCII table you can refer to

# 입력 == 출력
# Test.assert_equals(get_ascii("A"), 65)
# Test.assert_equals(get_ascii(" "), 32)
# Test.assert_equals(get_ascii("!"), 33)

# My Code
def get_ascii(c):
    return ord(c)

if __name__=='__main__':
    print(get_ascii("A"))
    print(get_ascii(" "))
    print(get_ascii("!"))

    # 숫자 -> 문자
    print(chr(65), type(chr(65)))
    # 문자 -> 숫자
    print(ord('A'), type(ord('A')))
    # 숫자를 2진수로 출력
    print(bin(ord('A')), type(bin(ord('A'))))
    # 숫자를 8진수로 출력
    print(oct(ord('A')), type(oct(ord('A'))))
    # 숫자를 16진수로 출력
    print(hex(ord('A')), type(hex(ord('A'))))

    # 2진수
    print(int('0b101010', 2))
    # 8진수
    print(int('0o52', 8))
    # 10진수
    print(int('42', 10))
    # 16진수
    print(int('0x2a', 16))

    # 접두어 없애기
    print(format(42, 'b'))
    print(format(42, 'o'))
    print(format(42, 'x'))
    print(format(42, 'X'))
    print(format(42, 'd'))

    # 접두어 포함시키기
    print(format(42, '#b'))
    print(format(42, '#o'))
    print(format(42, '#x'))
    print(format(42, '#X'))
    print(format(42, '#d'))
