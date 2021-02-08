# Hells Kitchen
# https://www.codewars.com/kata/57d1f36705c186d018000813/train/python

# 나의 풀이
def gordon0(a):
    answer = []
    for i in a.upper().split():
        tmp = ''
        for j in i:
            if j in 'EIOU':
                tmp += '*'
            elif j is 'A':
                tmp += '@'
            else:
                tmp += j
        answer.append(tmp+'!!!!')
    return ' '.join(answer)

def gordon1(a):
    return a.upper().replace('A', '@').replace('E', '*').replace('I', '*').replace("O", '*').replace('U', '*').replace(' ', '!!!! ') + '!!!!'

def gordon(a):
    return a.upper().translate(str.maketrans('AEIOU', '@****')).replace(' ', '!!!! ') + '!!!!'

# 다른 사람의 풀이
def gordon2(s):
    return " ".join(x + "!!!!" for x in s.upper().translate(str.maketrans("AIUEO", "@****")).split())

print(gordon('What feck damn cake'))
print('WH@T!!!! F*CK!!!! D@MN!!!! C@K*!!!!')
"""
print(gordon('are you stu pid'), '@R*!!!! Y**!!!! ST*!!!! P*D!!!!')
print(gordon('i am a chef'), '*!!!! @M!!!! @!!!! CH*F!!!!')
print(gordon('dont you talk tome'), 'D*NT!!!! Y**!!!! T@LK!!!! T*M*!!!!')
print(gordon('how dare you feck'), 'H*W!!!! D@R*!!!! Y**!!!! F*CK!!!!')
"""