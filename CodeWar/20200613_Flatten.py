# 문제
# Flatten
# Write a function that flattens an Array of Array objects into a flat Array.
# Your function must only do one level of flattening.

# 입력 == 출력
# Test.assert_equals(flatten([]) , [], "[]")
# Test.assert_equals(flatten([1,2,3]) , [1,2,3], "[1,2,3]")
# Test.assert_equals(flatten([[1,2,3],["a","b","c"],[1,2,3]]) , [1,2,3,"a","b","c",1,2,3], '[[1,2,3],["a","b","c"],[1,2,3]]')
# Test.assert_equals(flatten([[1,2,3],["a","b","c"],[1,2,3],"a"]) , [1,2,3,"a","b","c",1,2,3,"a"], '[[1,2,3],["a","b","c"],[1,2,3],"a"]')
# Test.assert_equals(flatten([[3,4,5],[[9,9,9]],["a,b,c"]]) , [3,4,5,[9,9,9],"a,b,c"], '[[3,4,5],[[9,9,9]],["a,b,c"]]')
# Test.assert_equals(flatten([[[3],[4],[5]],[9],[9],[8],[[1,2,3]]]) , [[3],[4],[5],9,9,8,[1,2,3]], '[[3,4,5],[[9,9,9]],["a,b,c"]]')

# My Code
def flatten(lst):
    answer = []
    for i in lst:
        if type(i) == list:
            answer.extend(i)
        else:
            answer.append(i)
    return answer

# Warriors Code
from itertools import chain
def flatten1(lst):
    try:
        return list(chain.from_iterable(lst))
    except:
        return lst

if __name__ == '__main__':
    print(flatten([]), [])
    print(flatten([1, 2, 3]), [1, 2, 3])
    print(flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]]), [1, 2, 3, "a", "b", "c", 1, 2, 3])
    print(flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3], "a"]), [1, 2, 3, "a", "b", "c", 1, 2, 3, "a"])
    print(flatten([[3, 4, 5], [[9, 9, 9]], ["a,b,c"]]), [3, 4, 5, [9, 9, 9], "a,b,c"])
    print(flatten([[[3], [4], [5]], [9], [9], [8], [[1, 2, 3]]]), [[3], [4], [5], 9, 9, 8, [1, 2, 3]])