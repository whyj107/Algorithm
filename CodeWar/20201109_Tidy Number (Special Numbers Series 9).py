def tidyNumber(n):
    return int(''.join(sorted(str(n)))) == n

print(tidyNumber(12), True)
print(tidyNumber(102), False)
print(tidyNumber(9672), False)
print(tidyNumber(2789), True)