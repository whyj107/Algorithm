# 문제
# In this kata you will create a function that takes
# a list of non-negative integers and strings and returns
# a new list with the strings filtered out.

# 입력 == 출력
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# --------------------------
# 타입을 확인하는 방법
# print type(변수)

# 인스턴스 비교 방법
# print isinstance(변수, 타입명)

# 형변환방법
# test = str(test)
# test = dict(test)
# --------------------------

# My Code
def filter_list(l):
    answer = []

    for j in l:
        if isinstance(j, int):
            answer.append(j)
    return answer

# Warriors Code
def filter_list_(l):
    return [i for i in l if not isinstance(i, str)]

if __name__=='__main__':
    l = filter_list([1, 2, 'a', 'b'])
    print(l)