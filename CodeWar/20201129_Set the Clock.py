# Set the Clock
# https://www.codewars.com/kata/5fbfc2c0dce9ec000de691e3/train/python

# 나의 풀이
def set_clock(time, buttons):
    h, m = map(int, time.split(':'))
    h += buttons.count('H')
    m += buttons.count('M')
    return f'{h%24 or 24}:{m%60:02}'

# 다른 사람의 풀이
def set_clock1(time, buttons):
    hour = (int(time.split(':')[0]) + buttons.count('H')) % 24
    min = (int(time.split(':')[1]) + buttons.count('M')) % 60
    return ('24' if hour == 0 else str(hour)) + ':' + ('0' + str(min) if min < 10 else str(min))

def set_clock2(time, buttons):
    h, m = map(int, time.split(':'))
    H = sum(x=='H' for x in buttons)
    M = len(buttons)-H
    return f"{(h+H)%24 or 24}:{(m+M)%60:02d}"

print(set_clock("9:21", ['M', 'M', 'M', 'M', 'H', 'H', 'M']), "11:26")
print(set_clock("16:54", ['M', 'M', 'H', 'M', 'M', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H', 'H']), "24:00")