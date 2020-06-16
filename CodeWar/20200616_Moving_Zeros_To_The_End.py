# 문제
# Moving Zeros To The End
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.

# 입력 == 출력
# Test.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
# Test.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
# Test.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
# Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
# Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
# Test.assert_equals(move_zeros(["a","b"]),["a","b"])
# Test.assert_equals(move_zeros(["a"]),["a"])
# Test.assert_equals(move_zeros([0,0]),[0,0])
# Test.assert_equals(move_zeros([0]),[0])
# Test.assert_equals(move_zeros([False]),[False])
# Test.assert_equals(move_zeros([]),[])

# My Code
def move_zeros(array):
    answer = []
    cnt = 0
    for i in array:
        if type(i) != bool and i == 0:
            cnt += 1
        else:
            answer.append(i)
    for i in range(cnt):
        answer.append(0)
    return answer

# Warriors Code
def move_zeros1(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

if __name__ == '__main__':
    print(type(False))
    print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    print(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])
    print(move_zeros(["a", "b"]), ["a", "b"])
    print(move_zeros(["a"]), ["a"])
    print(move_zeros([0, 0]), [0, 0])
    print(move_zeros([0]), [0])
    print(move_zeros([False]), [False])
    print(move_zeros([]), [])