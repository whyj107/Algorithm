# Even or Odd - Which is Greater?
# https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python

# 나의 풀이
def even_or_odd0(s):
    even, odd = 0, 0
    for i in s:
        n = int(i)
        if n % 2 == 0:
            even += n
        else:
            odd += n
    if even == odd:
        return 'Even and Odd are the same'
    elif even > odd:
        return 'Even is greater than Odd'
    else:
        return 'Odd is greater than Even'

def even_or_odd(s):
    even = sum(int(i) for i in s if int(i) % 2 == 0)
    odd = sum(int(i) for i in s if int(i) % 2 != 0)
    re = ['Even and Odd are the same', 'Even is greater than Odd', 'Odd is greater than Even']
    return re[0] if even == odd else (re[1] if even > odd else re[2])

# 다른 사람의 풀이
def even_or_odd1(s):
    o, e = sum(int(d) for d in s if int(d)%2),  sum(int(d) for d in s if not int(d)%2)
    return 'Even is greater than Odd'if e>o else 'Odd is greater than Even' if o>e else 'Even and Odd are the same'

print(even_or_odd('12'), 'Even is greater than Odd')
print(even_or_odd('123'), 'Odd is greater than Even')
print(even_or_odd('112'), 'Even and Odd are the same')