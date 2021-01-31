# 1RM Calculator
# https://www.codewars.com/kata/595bbea8a930ac0b91000130/train/python

# 나의 풀이
def calculate_1RM(w, r):
    answer = [round(w*(1 + r/30)), round((100*w)/(101.3 - 2.67123*r)), round(w*(r**0.10))]
    return 0 if 0 in answer else (w if r == 1 else max(answer))

# 다른 사람의 풀이
def calculate_1RM1(w, r):
    if r == 0: return 0
    if r == 1: return w

    return round(max([
        w * (1 + r / 30),  # Epley
        100 * w / (101.3 - 2.67123 * r),  # McGlothin
        w * r ** 0.10  # Lombardi
    ]))

print(calculate_1RM(135, 20), 282)
print(calculate_1RM(200, 8), 253)
print(calculate_1RM(270, 2), 289)
print(calculate_1RM(360, 1), 360)
print(calculate_1RM(400, 0), 0)