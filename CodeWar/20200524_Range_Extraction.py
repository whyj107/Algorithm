# 문제
# Range Extraction
# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
# The range includes all integers in the interval including both endpoints.
# It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
# Complete the solution so that it takes a list of integers in increasing order
# and returns a correctly formatted string in the range format.

# 입력 == 출력
# Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
# Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')

# My Code
def solution(args):
    answer = []
    start = args[0]
    pre_num = args[0]
    end = args[0]
    for i in range(1, len(args)):
        if pre_num + 1 == args[i]:
            pre_num = args[i]
            end = args[i]
            if args[i] != args[-1]:
                continue

        if start + 1 == end:
            answer.append(str(start))
            answer.append(str(end))
        elif start != end:
            answer.append(str(start) + '-' + str(end))
        else:
            answer.append(str(args[i - 1]))

        if args[i] != args[-1]:
            start = args[i]
            end = args[i]
            pre_num = args[i]

    if end != args[-1]:
        answer.append(str(args[-1]))

    return ','.join(answer)

def solution1(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n

    return ",".join(out)

if __name__ == '__main__':
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20, 22]),
          '-6,-3-1,3-5,7-11,14,15,17-20,22')
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]),
          '-3--1,2,10,15,16,18-20')