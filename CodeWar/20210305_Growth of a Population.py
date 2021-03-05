# Growth of a Population
# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

# 나의 풀이
def nb_year(p0, percent, aug, p):
    cnt = 0
    while p0 < p:
        p0 = int(p0 * (1+percent*0.01) + aug)
        cnt += 1
    return cnt

print(nb_year(1500, 5, 100, 5000), 15)
print(nb_year(1500000, 2.5, 10000, 2000000), 10)
print(nb_year(1500000, 0.25, 1000, 2000000), 94)
print(nb_year(1000, 2.0, 50, 1214), 4)
print(nb_year(1500000, 0.0, 10000, 2000000), 50)
