# A Cinema
# https://www.codewars.com/kata/603301b3ef32ea001c3395d0/train/python

# 나의 풀이
def cinema(b, g):
    answer = ''
    if max(b, g) > 2 * min(b, g):
        return None
    elif b == g:
        return 'GB' * b
    else:
        while b + g != 0:
            if b < g and b != 0:
                answer += 'GB'
                b -= 1
                g -= 1
            elif b > g and g != 0:
                answer += 'BG'
                b -= 1
                g -= 1
            if answer[-1] == 'B':
                answer += 'G'
                g -= 1
            else:
                answer += 'B'
                b -= 1
    return answer

# 다른 사람의 풀이
def cinema1(x, y):
    if 2*x >= y and 2*y >= x:
        return "BGB"*(x-y) + "GBG"*(y-x) + "BG"*(min(x, y)-abs(x-y))

def cinema2(b, g):
    x, y = max(b, g), min(b, g)
    if x > 2*y: return
    sx, sy = ('B', 'G') if b > g else ('G', 'B')
    return (sx+sy+sx) * (x-y) + (sy+sx) * (2*y-x)

print(cinema(1, 1), ["BG", "GB"])
# print(cinema(2, 2), ["BGBG", "GBGB", "GBBG", "BGGB"])
# print(cinema(2, 1), "BGB")
# print(cinema(1, 2), "GBG")
# print(cinema(10, 2), None)
# print(cinema(1, 3), None)
print(cinema(5, 7))
print(cinema(2, 3))