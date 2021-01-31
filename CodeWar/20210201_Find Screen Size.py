# Find Screen Size
# https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f/train/python

# 나의 풀이
def find_screen_height(width, ratio):
    w, h = map(int, ratio.split(':'))
    return f'{width}x{int(width*h/w)}'

# 다른 사람의 풀이
def find_screen_height1(width, ratio):
    a, b = map(int, ratio.split(':'))
    return f'{width}x{width * b // a}'

print(find_screen_height(1024, "4:3"), "1024x768")
print(find_screen_height(1280, "16:9"), "1280x720")
print(find_screen_height(3840, "32:9"), "3840x1080")