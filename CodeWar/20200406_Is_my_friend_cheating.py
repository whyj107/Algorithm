# 문제
# A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
# Within that sequence, he chooses two numbers, a and b.
# He says that the product of a and b should be equal to the sum of all numbers in the sequence,
# excluding a and b.
# Given a number n, could you tell me the numbers he excluded from the sequence?
# The function takes the parameter: n (n is always strictly greater than 0)
# and returns an array or a string (depending on the language) of the form:
# [(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
# with all (a, b) which are the possible removed numbers in the sequence 1 to n.
# [(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".
# It happens that there are several possible (a, b).
# The function returns an empty array (or an empty string)
# if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).
# (See examples of returns for each language in "RUN SAMPLE TESTS")

# 입력 == 출력
# test.assert_equals(removNb(100), [])
# test.assert_equals(removNb(26), [(15, 21), (21, 15)])

# My Code
def removNb(n):
    answer = []
    # 가우스의 법칙
    sum = int((n+1)*n/2)
    # a를 1부터 n 만큼 증가시키면서 b를 찾는다.
    for a in range(1, n+1):
        # b를 수식으로 정리하면 아래와 같다.
        # b = (sum - a - b ) // a
        b = (sum - a) // (a + 1)
        # b가 n보다 작고
        if b <= n:
            # 아래와 같은 조건을 만족하면
            if a * b == sum - a - b:
                # list에 저장한다.
                answer.append((a, b))
    return answer

# Warriors Code
def removNb_(n):
    s = n * (n + 1) / 2
    return [((s-a)//(a+1), a) for a in range(n-1, n//2, -1)  if (s-a) % (a+1) == 0]

if __name__=='__main__':
    answer = removNb(26)
    print(answer)
