# 문제
# Triangular Treasure
# Triangular numbers are so called because of the equilateral triangular shape
# that they occupy when laid out as dots. i.e.

# 입력 == 출력
# Test.assert_equals(triangular(2), 3)
# Test.assert_equals(triangular(4), 10)
# Test.assert_equals(triangular(9), 45)
# Test.assert_equals(triangular(-9), 0)

# My Code
# 시간이 오래 걸린다.
def triangular_(n):
    print(sum(range(1, n+1)))

def triangular(n):
    # 수학공식 이용
    return n * (n+1) // 2 if n > 0 else 0

if __name__ == '__main__':
    # lambda 이용
    triangular1 = lambda n: (n + n ** 2) / 2 if n > 0 else 0

    print(triangular(2), 3)
    print(triangular(4), 10)
    print(triangular(9), 45)
    print(triangular(744883645), 277425822666684835)