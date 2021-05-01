n = range(1, 51)
n = filter(lambda i: i % 2 > 0 or i % 5 > 0, n)
n = list(n)

answer = []
k = 1
while len(n) > 0:
    x = int("{0:b}".format(k)) * 7
    """
    if '0' in str(x):
        for i in n:
            if x % i == 0:
                if str(x) == str(x)[::-1]:
                    answer.append(i)
                n.remove(i)
    """
    for i in n:
        if x % i == 0:
            if str(x) == str(x)[::-1]:
                answer.append(i)
            n.remove(i)
    k += 1

answer.sort()
print(answer)