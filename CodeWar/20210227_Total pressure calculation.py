# Total pressure calculation
# https://www.codewars.com/kata/5b7ea71db90cc0f17c000a5a/train/python

# 이건 그냥 물리 문제이다.

# 나의 풀이
# Ptotal = (m1/M1 + m2/M2)*R*T/V
def solution(M1, M2, m1, m2, V, T) :
    return (m1/M1 + m2/M2)*0.082*(T+273.15)/V

print(solution(44, 30, 3, 2, 5, 50), 0.7146511212121212);
print(solution(60, 20, 10, 30, 10, 100), 5.099716666666667);
