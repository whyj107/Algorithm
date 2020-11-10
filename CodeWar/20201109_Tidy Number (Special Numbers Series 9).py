# Tidy Number (Special Numbers Series #9)
# https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python

# 나의 풀이
def tidyNumber(n):
    return int(''.join(sorted(str(n)))) == n

print(tidyNumber(12), True)
print(tidyNumber(102), False)
print(tidyNumber(9672), False)
print(tidyNumber(2789), True)
