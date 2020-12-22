# Dollars and Cents
# https://www.codewars.com/kata/55902c5eaa8069a5b4000083/train/python

# 나의 풀이
def format_money(amount):
    return f'${amount:.2f}'

# 다른 사람의 풀이
def format_money1(amount):
    return '${:.2f}'.format(amount)

def format_money2(amount):
    return '$%0.2f' % amount

print(format_money(39.99), '$39.99')