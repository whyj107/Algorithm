# 문제
# N-th Fibonacci
# I love Fibonacci numbers in general, but I must admit I love some more than others.
#
# I would like for you to write me a function that when given a number (n)
# returns the n-th number in the Fibonacci Sequence.

# My Code
def nth_fib(n):
    answer = [0, 1]
    for i in range(n-1):
        answer.append(answer[i] + answer[i + 1])
    return answer[n-1]

# Warriors Code
def nth_fib1(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    print(nth_fib(4), 2)