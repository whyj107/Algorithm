# Beginner Series #4 Cockroach
# https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6/train/python

# 나의 풀이
def cockroach_speed(s):
    return int(round(s/1.08*30, 3))

# 다른 사람의 풀이
def cockroach_speed1(s):
    return s // 0.036

def cockroach_speed2(s):
    cm_per_km = 100000
    sec_per_hour = 3600
    return int(s * cm_per_km / sec_per_hour)

print(cockroach_speed(1.08), 30)
print(cockroach_speed(1.09), 30)
print(cockroach_speed(0), 0)