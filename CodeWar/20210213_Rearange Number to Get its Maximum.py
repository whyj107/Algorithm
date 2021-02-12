# Rearange Number to Get its Maximum
# https://www.codewars.com/kata/563700da1ac8be8f1e0000dc/train/python

# 나의 풀이
def max_redigit(num):
    return int(''.join(sorted(list(str(num)), reverse=True))) if 99 < num < 1000 else None

# 다른 사람의 풀이
def max_redigit1(num):
    if isinstance(num, int) and 99 < num < 1000:
        return int("".join(sorted(str(num), reverse=True)))

print(max_redigit(123), 321)
print(max_redigit(555), 555)
print(max_redigit(-1), None)
print(max_redigit(0), None)
print(max_redigit(99), None)
print(max_redigit(1000), None)