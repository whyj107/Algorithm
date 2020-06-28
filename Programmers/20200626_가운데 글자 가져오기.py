# 문제
# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

# 나의 풀이
def solution(s):
    return s[len(s)//2 - 1:len(s)//2 + 1] if len(s) %2 == 0 else s[len(s)//2]

# 다른 사람의 풀이
def string_middle1(str):
    return str[(len(str)-1)//2:len(str)//2+1]

if __name__ == '__main__':
    print(solution('abcde'), 'c')
    print(solution('qwer'), 'we')