# 문제
# Collatz
# https://www.codewars.com/kata/5286b2e162056fd0cb000c20/train/python

# 나의 풀이
def collatz(n):
    answer = str(n)
    while n != 1:
        answer += '->'
        if n%2 == 0:
            n //= 2
        else:
            n = (3*n + 1)
        answer += str(n)
    return answer

# 다른 사람의 풀이
def collatz1(n):
    l = [str(n)]
    while n > 1:
        n = 3 * n + 1 if n % 2 else n / 2
        l.append(str(n))
    return '->'.join(l)

if __name__ == '__main__':
    print(collatz(3), "3->10->5->16->8->4->2->1");