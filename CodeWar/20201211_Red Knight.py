# Red Knight
# https://www.codewars.com/kata/5fc4349ddb878a0017838d0f/train/python

# 나의 풀이
def red_knight(N, P):
    return ('White' if (N == 0 and P%2 == 0) or (N==1 and P%2 != 0) else 'Black', P*2)

# 다른 사람의 풀이
def red_knight1(N, P):
    return ('White' if P % 2 == N else 'Black', P * 2)

def red_knight2(N, P):
    return (['White','Black'][(N+P)%2],2*P)

print(red_knight(0, 8), ('White', 16))
print(red_knight(0, 7), ('Black', 14))
print(red_knight(1, 6), ('Black', 12))
print(red_knight(1, 5), ('White', 10))