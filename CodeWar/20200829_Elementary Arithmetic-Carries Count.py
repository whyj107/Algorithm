# 문제
# Elementary Arithmetic - Carries Count
# https://www.codewars.com/kata/529fdef7488f509b81000061/train/python

# 나의 풀이
def solve(input_string):
    answer = []
    for n in input_string.split('\n'):
        carry, carried = 0, 0
        A, B = map(str, n[::-1].split())
        for x in range(len(A)):
            carried += (int(A[x])+int(B[x]))
            carry += carried > 9
            carried //= 10
        answer.append(carry)
    return '\n'.join("No carry operation" if not c else "%d carry operations" % c for c in answer)


# 다른 사람의 풀이
def solve1(input_string):
    ans = []
    for ab in input_string.split('\n'):
        carry, carried = 0, 0
        for a, b in zip(*map(lambda ss: map(int, ss[::-1]), ab.split())):
            carried += a+b
            carry += carried > 9
            carried //= 10
        ans.append(carry)

    return '\n'.join("No carry operation" if not c else "%d carry operations" % c for c in ans)

if __name__ == "__main__":
    print(solve("123 456\n555 555\n123 594"), "No carry operation\n3 carry operations\n1 carry operations",
                       "Try this one: (123 - 456 | 555 - 555 | 123 - 594)")
    """
    print(solve("321 679\n098 805\n123 867"), "3 carry operations\n2 carry operations\n1 carry operations",
                       "Try this one: (321 - 679 | 098 - 805 | 123 - 867)")
    print(solve("123 457\n631 372\n999 111"), "1 carry operations\n2 carry operations\n3 carry operations",
                       "Try this one: (123 - 457 | 631 - 372 | 999 - 111)")
    print(solve("123 457\n123 456\n654 312\n999 000\n123 457"),
                       "1 carry operations\nNo carry operation\nNo carry operation\nNo carry operation\n1 carry operations",
                       "Try this one: (123 - 457 | 123 - 456 | 654 - 312 | 999 - 000 | 123 - 457)")
    print(solve("1 9\n123456789 111111101\n01 09\n11 09\n123 457"),
                       "1 carry operations\n1 carry operations\n1 carry operations\n1 carry operations\n1 carry operations",
                       "Try this one: (1 - 9 | 123456789 - 111111101 | 01 - 09 | 11 - 09 | 123 - 457)")
    print(solve("99 99"), "2 carry operations", "Try this one: (99 - 99)")
    """