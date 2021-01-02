# Buying a car
# https://www.codewars.com/kata/554a44516729e4d80b000012/train/python

# 나의 풀이
def nbMonths(o, n, s, l):
    cnt, result = 0, n
    if o >= n: return [cnt, o-n]
    while result > 0:
        cnt += 1
        rate = 1-l*0.01
        n *= rate
        o *= rate
        result = n - o - s*cnt
        if cnt % 2 != 0: l += 0.5
    return [cnt, round(-result)]

# 다른 사람의 풀이
def nbMonths1(old, new, saving, percent):
    month = 0
    while old - new + saving * month < 0:
        month += 1
        devalue = (100.0 - percent - 0.5 * (month / 2)) / 100.0
        old *= devalue
        new *= devalue
    return [month, round(old - new + saving * month)]

def nbMonths2(old, new, saving, percent):
    diff, m = old - new, 0
    while diff + saving * m < 0:
        m += 1
        diff *= (100.0 - percent - 0.5 * (m / 2)) / 100.0
    return [m, round(diff + saving * m)]

print(nbMonths(2000, 8000, 1000, 1.5), [6, 766])
print(nbMonths(12000, 8000, 1000, 1.5), [0, 4000])