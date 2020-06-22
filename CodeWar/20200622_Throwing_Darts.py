# 문제
# Throwing Darts
# You've just recently been hired to calculate scores for a Dart Board game!
#
# Scoring specifications:
#
# 0 points - radius above 10
# 5 points - radius between 5 and 10 inclusive
# 10 points - radius less than 5
# If all radii are less than 5, award 100 BONUS POINTS!
#
# Write a function that accepts an array of radii (can be integers and/or floats),
# and returns a total score using the above specification.
#
# An empty array should return 0.

# 입력 == 출력
# Test.assert_equals(score_throws([1, 5, 11]), 15)
# Test.assert_equals(score_throws([15, 20, 30, 31, 32, 44, 100]),  0)
# Test.assert_equals(score_throws([1, 2, 3, 4]), 140)
# Test.assert_equals(score_throws([]), 0, 'Empty list')
# Test.assert_equals(score_throws([1, 2, 3, 4, 5, 6, 7, 8, 9]), 65)
# Test.assert_equals(score_throws([0, 5, 10, 10.5, 4.5]),  30)
# Test.assert_equals(score_throws([1]), 110)
# Test.assert_equals(score_throws([21, 10, 10]), 10)
# Test.assert_equals(score_throws([5, 5, 5, 5]), 20)
# Test.assert_equals(score_throws([4.9, 5.1]),  15)

# My Code
def score_throws(radii):
    answer = 0
    cnt = 0
    for i in radii:
        if i < 5:
            answer += 10
            cnt += 1
        elif i <= 10:
            answer += 5
        else:
            answer += 0
        if cnt == len(radii):
            answer += 100
    return answer

# Warriors Code
def score_throws1(radii):
    score = sum(10 if r < 5 else 5 if r <= 10 else 0 for r in radii)
    return score + 100 if score and len(radii) * 10 == score else score

if __name__ == '__main__':
    print(score_throws([1, 5, 11]), 15)
    print(score_throws([15, 20, 30, 31, 32, 44, 100]), 0)
    print(score_throws([1, 2, 3, 4]), 140)
    print(score_throws([]), 0, 'Empty list')
    print(score_throws([1, 2, 3, 4, 5, 6, 7, 8, 9]), 65)
    print(score_throws([0, 5, 10, 10.5, 4.5]), 30)
    print(score_throws([1]), 110)
    print(score_throws([21, 10, 10]), 10)
    print(score_throws([5, 5, 5, 5]), 20)
    print(score_throws([4.9, 5.1]), 15)