# Easy wallpaper
# https://www.codewars.com/kata/567501aec64b81e252000003/train/python

# 나의 풀이
# and를 사용하면 min 값을 나타내는 것과 같다.
from math import ceil
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
def wallpaper(l, w, h):
    return numbers[ceil(l and w and ((l + w) * h * 2 * 1.15) / 5.2)]

print(wallpaper(6.3, 4.5, 3.29), "sixteen")
print(wallpaper(7.8, 2.9, 3.29), "sixteen")
print(wallpaper(6.3, 5.8, 3.13), "seventeen")
print(wallpaper(6.1, 6.7, 2.81), "sixteen")