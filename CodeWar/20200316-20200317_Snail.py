# 문제
# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements
# to the middle element, traveling clockwise.
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# 입력 == 출력
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# expected = [1,2,3,6,9,8,7,4,5]
# test.assert_equals(snail(array), expected)
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# expected = [1,2,3,4,5,6,7,8,9]
# test.assert_equals(snail(array), expected)

# --------------------------
# 어렵다 어려워
# del 리스트[인덱스] : 리스트의 해당 인덱스 원소 삭제
# 리스트.remove(원소) : 리스트 a의 해당 원소 삭제
# zip(*iterable) : 동일한 개수로 이루어진 자료형을 묶어 주는 역할
#                  list(zip([1, 2, 3], [4, 5, 6]))
#                  ==> [(1, 4), (2, 5), (3, 6)]
# --------------------------

# My Code
def snail_(snail_map):
    result = []
    while len(snail_map) > 0:
        # 오른쪽으로
        result += snail_map[0]
        del snail_map[0]

        if len(snail_map) > 0:
            # 아래쪽으로
            for i in snail_map:
                result += [i[-1]]
                del i[-1]

            # 왼쪽으로
            if snail_map[-1]:
                result += snail_map[-1][::-1]
                del snail_map[-1]

            # 위쪽으로
            for i in reversed(snail_map):
                result += [i[0]]
                del i[0]
    return result

# Warriors Code
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1]
    return out

if __name__=='__main__':
    answer = snail([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    print(answer)
    # 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
