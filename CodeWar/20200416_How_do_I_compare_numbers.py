# 문제
# What could be easier than comparing integer numbers?
# However, the given piece of code doesn't recognize some of the special numbers
# for a reason to be found. Your task is to find the bug and eliminate it.

# 입력 == 출력
# tests = [
#     (0, 'nothing'),
#     (123, 'nothing'),
#     (-1, 'nothing'),
#     (42, 'everything'),
#     (42 * 42, 'everything squared'),
# ]

# My Code
def what_is(x):
    print(x)
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

if __name__=='__main__':
    answer = what_is(0)
    print(answer)
    answer = what_is(123)
    print(answer)
    answer = what_is(-1)
    print(answer)
    answer = what_is(42)
    print(answer)
    answer = what_is(42 * 42)
    print(answer)