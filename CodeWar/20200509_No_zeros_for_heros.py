# 문제
# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.

# 입력 == 출력
# testing(no_boring_zeros(1450), 145)
# testing(no_boring_zeros(960000), 96)
# testing(no_boring_zeros(1050), 105)
# testing(no_boring_zeros(-1050), -105)
# testing(no_boring_zeros(0), 0)

# My Code
def no_boring_zeros(n):
    if n % 10 == 0 and n != 0:
        while n % 10 == 0:
            n //= 10
        return n
    else:
        return n

def no_boring_zeros1(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0

if __name__=='__main__':
    print(no_boring_zeros(1450))
    print(no_boring_zeros(960000))
    print(no_boring_zeros(1050))
    print(no_boring_zeros(-1050))
    print(no_boring_zeros(0))