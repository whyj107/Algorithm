# 문제
# Return substring instance count
# Complete the solution so that it returns the number of times
# the search_text is found within the full_text.

# 입력 == 출력
# test.assert_equals(solution('abcdeb','b'), 2)
# test.assert_equals(solution('abc','b'), 1)
# test.assert_equals(solution('abbc','bb'), 1)

# My Code
def solution(full_text, search_text):
    return len(full_text.split(search_text)) - 1 if search_text != "" else len(full_text)+1

def solution1(full_text, search_text):
    return full_text.count(search_text)
if __name__ == '__main__':
    print(solution('mqBPFmtGTFasUrfJRyadyunzYtxAxuwwvkMQqNZtAuoQFxqZmIbfauxQHjoSCSjfkQsJkONeIyqYlxtfmevJaYSFYvWnymDixI', 'n'))
    print(solution('abc', 'b'), 1)
    print(solution('abbc', 'bb'), 1)
    print(solution('SVRV', 'dnL'))
    print(solution('cytCgfOZKULdAAdWTCQlOLmIQFTSlkVdHYzovcLVVVirbyqlhggEppMBHZNdpuGhfrumPtatJbUGswHkOYwgia', 'z'))
    print(solution('cvKiTpojTteDYWRoJrIrVgXtFvYxFcTRCHjOAPxMdAqepWocRvDBNqfMPnBXFMJBQlFAqBnmyy', 'V'))