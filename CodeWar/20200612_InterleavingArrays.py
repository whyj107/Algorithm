# 문제
# Interleaving Arrays
# Create a function, that accepts an arbitrary number of arrays and returns a single array generated by alternately appending elements from the passed in arguments. If one of them is shorter than the others, the result should be padded with empty elements.

# 입력 == 출력
# Test.assert_equals(interleave([1, 2, 3], ["c", "d", "e"]), [1, "c", 2, "d", 3, "e"])
# Test.assert_equals(interleave([1, 2, 3], [4, 5]), [1, 4, 2, 5, 3, None])
# Test.assert_equals(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])
# Test.assert_equals(interleave([]), [])

# My Code
def interleave(*args):
    answer = []
    args_len = max([len(i) for i in args])
    for i in args:
        if len(i) < args_len:
            for j in range(args_len - len(i)):
                i.append(None)
    for i in zip(*args):
        answer.extend(i)
    return answer

# Warriors Code
from itertools import chain, zip_longest
def interleave1(*args):
    return list(chain.from_iterable(zip_longest(*args)))


def interleave2(*args):
    max_len = max(map(len, args))
    interleaved = []

    for i in range(max_len):
        for arr in args:
            if i < len(arr):
                interleaved.append(arr[i])
            else:
                interleaved.append(None)

    return interleaved

if __name__ == '__main__':
    print(interleave([1, 2, 3], ["c", "d", "e"]), [1, "c", 2, "d", 3, "e"])
    print(interleave([1, 2, 3], [4, 5]), [1, 4, 2, 5, 3, None])
    print(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 6, 9])
    print(interleave([]), [])