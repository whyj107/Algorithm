# 문제
# [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3

# 나의 풀이
def solution(dartResult):
    answer = 0
    pre_num = 0
    num = 0
    tmp = {'S': lambda x: x, 'D': lambda x: x**2, 'T': lambda x: x**3,
           '*': lambda x: 2*x, '#': lambda x: -x}
    for idx, i in enumerate(dartResult+'!'):
        if i.isdigit():
            if dartResult[idx-1].isdigit():
                num = int(str(num)+i)
            else:
                answer += num
                pre_num, num = num, int(i)
        elif i in ['S', 'D', 'T', '#']:
            num = tmp[i](num)
        elif i in ['*']:
            answer += pre_num
            num = (tmp[i](num))
        else:
            answer += num
    return answer

# 다른 사람의 풀이
import re

def solution1(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

if __name__ == '__main__':
    print(solution("1S2D*3T"), 37)
    print(solution("1D2S#10S"), 9)
    print(solution("1D2S0T"), 3)
    print(solution("1S*2T*3S"), 23)
    print(solution("1D#2S*3S"), 5)
    print(solution("1T2D3D#"), -4)
    print(solution("1D2S3T*"), 59)