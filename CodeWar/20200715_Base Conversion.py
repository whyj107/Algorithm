# 문제
# Base Conversion

bin = '01'
oct = '01234567'
dec = '0123456789'
hex = '0123456789abcdef'
allow = 'abcdefghijklmnopqrstuvwxyz'
allup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# My Code
def convert(input, source, target):
    s = 0
    cnt = 0
    for i in input[::-1]:
        s += (source.index(i) * (len(source) ** cnt))
        cnt += 1
    answer = ""
    if s == 0:
        answer = target[s]
    while s > 0:
        answer += target[(s % len(target))]
        s //= len(target)
    return answer[::-1]

# Warriors Code
def convert1(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        acc *= base_in
        acc += source.index(d)
    while acc != 0:
        d = target[acc%base_out]
        acc = acc/base_out
        out = d+out
    return out if out else target[0]

if __name__ == '__main__':
    print(convert("15", dec, bin), '1111');
    print(convert("15", dec, oct), '17');
    print(convert("1010", bin, dec), '10');
    print(convert("1010", bin, hex), 'a');
    print(convert("0", dec, alpha), 'a');
    print(convert("27", dec, allow), 'bb');
    print(convert("hello", allow, hex), '320048')
    print(convert("SAME", allup, allup), 'SAME');