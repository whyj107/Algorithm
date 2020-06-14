# 문제
# Sequences and Series
# Can you find a pattern in it?
# If so, then write a function getScore(n)/get_score(n)/GetScore(n)
# which returns the score for any positive number n:
#
# int getScore(1) = return 50;
# int getScore(2) = return 150;
# int getScore(3) = return 300;
# int getScore(4) = return 500;
# int getScore(5) = return 750;

# 입력 == 출력
# test.expect(get_score(1) == 50, 'get_score(1) returns a wrong result')
# test.expect(get_score(2) == 150, 'get_score(2) returns a wrong result')
# test.expect(get_score(3) == 300, 'get_score(3) returns a wrong result')
# test.expect(get_score(4) == 500, 'get_score(4) returns a wrong result')
# test.expect(get_score(5) == 750, 'get_score(5) returns a wrong result')

# My Code
def get_score(n):
    answer = [0] * (n + 1)
    for i in range(1, n + 1):
        answer[i] = answer[i - 1] + (50 * i)
    return answer[-1]

# Warriors Code
def get_score1(n):
    return n * (n + 1) * 25

if __name__ == '__main__':
    print(get_score(1), 50)
    print(get_score(2), 150)
    print(get_score(3), 300)
    print(get_score(4), 500)
    print(get_score(5), 750)