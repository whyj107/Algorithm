# 문제
# Beeramid
# Let's pretend your company just hired your friend from college
# and paid you a referral bonus. Awesome!
# To celebrate, you're taking your team out to the terrible dive bar next door
# and using the referral bonus to buy, and build,
# the largest three-dimensional beer can pyramid you can.
# And then probably drink those beers, because let's pretend it's Friday too.
#
# A beer can pyramid will square the number of cans in each level - 1 can in the top level,
# 4 in the second, 9 in the next, 16, 25...
#
# Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make,
# given the parameters of:
# 1) your referral bonus, and
# 2) the price of a beer can

# 입력 == 출력
# Test.assert_equals(beeramid(9, 2),  1)
# Test.assert_equals(beeramid(21, 1.5),  3)
# Test.assert_equals(beeramid(-1, 4), 0)

# My Code
def beeramid(bonus, price):
    pyramid = []
    pyramid_tmp = 0
    cnt = 1
    if bonus < price:
        return 0
    while pyramid_tmp <= (bonus//price):
        pyramid.append(cnt*cnt)
        pyramid_tmp = sum(pyramid)
        cnt += 1
    return len(pyramid) - 1

# Warriors Code
def beeramid1(bonus, price):
    beers = bonus // price
    levels = 0

    while beers >= (levels + 1) ** 2:
        levels += 1
        beers -= levels ** 2

    return levels

if __name__ == '__main__':
    print(beeramid(9, 2), 1)
    print(beeramid(21, 1.5), 3)
    print(beeramid(-1, 4), 0)