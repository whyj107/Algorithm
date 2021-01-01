# Drawing a Cross!
# https://www.codewars.com/kata/5a036ecb2b651d696f00007c/train/python

# 나의 풀이
def draw_a_cross(n):
    re = ['Not possible to draw cross for grids less than 3x3!', 'Centered cross not possible!']
    if n < 3:
        return re[0]
    elif n % 2 == 0:
        return re[1]
    else:
        answer = ""
        for i in range(n//2):
            answer += " " * i + 'x' + " " * (n - 2*(i+1)) + 'x' + " " * i + "\n"
        answer += " "*(n//2) + "x" + " "*(n//2) + "\n"
        for i in range(n // 2):
            answer += " " * (n//2 - (i+1)) + 'x' + " " * (2*i + 1) + 'x' + " " * (n//2 - (i+1)) + "\n"
        return answer[:-1]

# 다른 사람의 풀이
def draw_a_cross1(n: int) -> str:
    if n < 3:
        return "Not possible to draw cross for grids less than 3x3!"
    if n % 2 == 0:
        return "Centered cross not possible!"
    lines = [('x' + ' ' * i + 'x').center(n) for i in range(n - 2, 0, -2)]
    return '\n'.join(lines + ['x'.center(n)] + lines[::-1])

print(draw_a_cross(7))
print('x     x\n x   x \n  x x  \n   x   \n  x x  \n x   x \nx     x')
print(draw_a_cross(15), 'x             x\n x           x \n  x         x  \n   x       x   \n    x     x    \n     x   x     \n      x x      \n       x       \n      x x      \n     x   x     \n    x     x    \n   x       x   \n  x         x  \n x           x \nx             x')
print(draw_a_cross(25), 'x                       x\n x                     x \n  x                   x  \n   x                 x   \n    x               x    \n     x             x     \n      x           x      \n       x         x       \n        x       x        \n         x     x         \n          x   x          \n           x x           \n            x            \n           x x           \n          x   x          \n         x     x         \n        x       x        \n       x         x       \n      x           x      \n     x             x     \n    x               x    \n   x                 x   \n  x                   x  \n x                     x \nx                       x', 'Should draw a centered cross in a grid of height and width n!')
print(draw_a_cross(6) , 'Centered cross not possible!')
print(draw_a_cross(10), 'Centered cross not possible!')
print(draw_a_cross(2), 'Not possible to draw cross for grids less than 3x3!')