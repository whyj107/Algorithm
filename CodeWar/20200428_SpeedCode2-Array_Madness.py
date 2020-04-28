# 문제
# Given two integer arrays a, b, both of length >= 1,
# create a program that returns true
# if the sum of the squares of each element in a is strictly greater than
# the sum of the cubes of each element in b.

# 입력 == 출력
# test.assert_equals(array_madness([4, 5, 6], [1, 2, 3]),True)
# test.assert_equals(array_madness( [1, 2, 3],[4, 5, 6]),False)

# My Code
def array_madness(a, b):
    # 2 제곱 list 생성
    a_tmp = [i * i for i in a]

    # 3 제곱 list 생성
    b_tmp = [i * i * i for i in b]

    # 2 제곱의 합과 3 제곱 합 비교 하여 2제곱이 크면 True 반환 아니면 False 반환
    if sum(a_tmp) > sum(b_tmp):
        return True
    else:
        return False

    # 한줄로 표현할 때
    return True if sum([i*i for i in a]) > sum([i*i*i for i in b]) else False

if __name__=='__main__':
    print(array_madness([4, 5, 6], [1, 2, 3]))
    print(array_madness([1, 2, 3], [4, 5, 6]))