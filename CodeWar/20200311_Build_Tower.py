# 문제
# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
#
# Tower block is represented as *
# Python: return a list;

# 입력 == 출력
# test.describe("Tests")
# test.it("Basic Tests")
# test.assert_equals(tower_builder(1), ['*', ])
# test.assert_equals(tower_builder(2), [' * ', '***'])
# test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])

# --------------------------
# --------------------------

# My Code
def tower_builder(n_floors):
    answer = []
    for i in range(n_floors):
        star = '*' * (i * 2 + 1)
        space = ' ' * (n_floors-(i+1))
        answer.append(space+star+space)
    return answer

# Warriors Code
def tower_builder_(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]

if __name__=='__main__':
    l = tower_builder(5)
    print(l)