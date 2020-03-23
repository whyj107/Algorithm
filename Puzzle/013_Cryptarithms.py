# 복면산을 만족하게 하는 것은 몇 가지일까?

# 문제
# 다음의 식을 만족하는 숫자 대입 방법을 몇 가지 있는지 구해 보세요.
# READ + WRITE + TALK = SKILL

from itertools import permutations
"""
count = 0
for (r, e, a, d, w, i, t, l, k, s) in permutations(range(0, 10)):
    if r == 0 or w == 0 or t == 0 or s == 0:
        continue
    read = r * 1000 + e * 100 + a * 10 + d
    write = w * 10000 + r * 1000 + i * 100 + t * 10 + e
    talk = t * 1000 + a * 100 + l * 10 + k
    skill = s * 10000 + k * 1000 + i * 100 + l * 10 + l
    if read + write + talk == skill:
        count += 1
        print("{} + {} + {} = {}".format(read, write, talk, skill))
print(count)
"""
# --------------------------------------------------------
# 속도가 아래가 더빠름

count = 0
for (e, a, d, t, k, l) in permutations(range(0, 10), 6):
    if ((a + t == 8) or (a + t == 9) or (a + t == 10)) and ((a + e == 8) or (a + e == 9) or (a + e == 10)) and ((d + e + k) % 10 == l) and (((a + t + l) * 10 + d + e + k) % 100 == l * 11):
        temp = [item for item in range(0, 10) if item not in [k, e, d, l, t, a]]
        for (i, r, s, w) in permutations(temp, 4):
            if ((r != 0) and (w != 0) and (t != 0)) and ((s == w + 1) or (s == w + 2)):
                read = r * 1000 + e * 100 + a * 10 + d
                write = w * 10000 + r * 1000 + i * 100 + t * 10 + e
                talk = t * 1000 + a * 100 + l * 10 + k
                skill = s * 10000 + k * 1000 + i * 100 + l * 10 + l
                if read + write + talk == skill:
                    print("{} + {} + {} = {}".format(read, write, talk, skill))
                    count += 1
print(count)