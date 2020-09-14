# 문제
# How Many Reindeers?
# https://www.codewars.com/kata/52ad1db4b2651f744d000394/train/python

# 나의 풀이
import math
def reindeer(presents):
    if presents > 180:
        raise
    return 2 + math.ceil(presents/30)
if __name__ == '__main__':
    print(reindeer(1))