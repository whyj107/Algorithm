# 문제
# Convert PascalCase string into snake_case
# https://www.codewars.com/kata/529b418d533b76924600085d/train/python

# 나의 풀이
def to_underscore(string):
    s_idx = 0
    answer = []
    for i in range(1, len(str(string))):
        if str(str(string)[i]).isupper():
            answer.append(str(string)[s_idx:i].lower())
            s_idx = i
    answer.append(str(string)[s_idx:].lower())
    return '_'.join(answer)

# 다른 사람의 풀이
import re
def to_underscore1(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()

if __name__ == '__main__':
    print(to_underscore('TestController'), 'test_controller')
    print(to_underscore(5), '5')
