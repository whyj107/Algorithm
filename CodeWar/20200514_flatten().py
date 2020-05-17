# 문제
# flatten()
# For this exercise you will create a global flatten method.
# The method takes in any number of arguments and flattens them into a single array.
# If any of the arguments passed in are an array then the individual objects within the array will be flattened
# so that they exist at the same level as the other arguments.
# Any nested arrays, no matter how deep, should be flattened into the single array result.

# 입력 == 출력
# test.assert_equals(flatten(),[])
# test.assert_equals(flatten(1,2,3),[1,2,3])
# test.assert_equals(flatten([1,2],[3,4,5],[6,[7],[[8]]]),[1,2,3,4,5,6,7,8])
# test.assert_equals(flatten(1,2,['9',[],[]],None),[1,2,'9',None])
# test.assert_equals(flatten(['hello',2,['text',[4,5]]],[[]],'[list]'),['hello',2,'text',4,5,'[list]'])

# My Code
def flatten(*ary):
    answer = []
    for i in ary:
        if type(i) == list:
            tmp = flatten(*i)
            for j in tmp:
                answer.append(j)
        else:
            answer.append(i)
    return answer

# Warriors Code
def flatten1(*a):
    r = []
    for x in a:
        if isinstance(x, list):
            r.extend(flatten(*x))
        else:
            r.append(x)
    return r

if __name__ == '__main__':
    print(flatten(), [])
    print(flatten(1, 2, 3), [1, 2, 3])
    print(flatten([1, 2], [3, 4, 5], [6, [7], [[8]]]), [1, 2, 3, 4, 5, 6, 7, 8])
    print(flatten(1, 2, ['9', [], []], None), [1, 2, '9', None])
    print(flatten(['hello', 2, ['text', [4, 5]]], [[]], '[list]'), ['hello', 2, 'text', 4, 5, '[list]'])
