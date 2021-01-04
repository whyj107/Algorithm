# How much water do I need?
# https://www.codewars.com/kata/575fa9afee048b293e000287/train/python

# 나의 풀이
# 문제 설명이 좋지 않은 문제였다.
def how_much_water(water, load, clothes):
    result = ['Too much clothes', 'Not enough clothes']
    if 2*load < clothes:
        return result[0]
    elif load > clothes:
        return result[1]
    return round(water*1.1**(clothes-load), 2)

print(how_much_water(10, 10, 21), 'Too much clothes')
print(how_much_water(10, 10, 2), 'Not enough clothes')
print(how_much_water(10, 11, 20), 23.58)
print(how_much_water(50, 15, 29), 189.87)