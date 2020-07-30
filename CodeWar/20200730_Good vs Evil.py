# 문제
# Good vs Evil
# https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python

# 나의 풀이
g = {0: 1,1: 2, 2: 3, 3: 3, 4: 4, 5: 10}
e = {0: 1,1: 2, 2: 2, 3: 2, 4: 3, 5: 5, 6:10}
def goodVsEvil(good, evil):
    good = sum([int(i)*g[idx] for idx, i in enumerate(good.split(" "))])
    evil = sum([int(i)*e[idx] for idx, i in enumerate(evil.split(" "))])
    return 'Battle Result: No victor on this battle field' if good == evil else('Battle Result: Good triumphs over Evil' if good > evil else 'Battle Result: Evil eradicates all trace of Good')

# 다른 사람의 풀이
def goodVsEvil1(good, evil):
    points_good = [1, 2, 3, 3, 4, 10]
    points_evil = [1, 2, 2, 2, 3, 5, 10]

    good = sum([int(x) * y for x, y in zip(good.split(), points_good)])
    evil = sum([int(x) * y for x, y in zip(evil.split(), points_evil)])

    result = 'Battle Result: '

    if good < evil:
        return result + 'Evil eradicates all trace of Good'
    elif good > evil:
        return result + 'Good triumphs over Evil'
    else:
        return result + 'No victor on this battle field'

if __name__ == '__main__':
    print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')=='Battle Result: Evil eradicates all trace of Good')
    print(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0')=='Battle Result: Good triumphs over Evil')
    print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0')=='Battle Result: No victor on this battle field')