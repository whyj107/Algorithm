# 문제
# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

# 입력 == 출력
# Test.assert_equals(positive_sum([1,2,3,4,5]),15)
# Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
# Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)
# Test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)

# My Code
def positive_sum(arr):
    sum = 0
    for i in arr:
        if i >= 0:
            sum += i
    return sum

# Warriors Code
def positive_sum_(arr):
    return sum(x for x in arr if x > 0)

if __name__=='__main__':
    answer = positive_sum([1, 2, 3, -1])
    print(answer)