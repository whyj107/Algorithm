# 문제
# Valid Braces
# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

# 나의 풀이
def validBraces(string):
    tmp = {")": "(", "}": "{", "]": "["}
    answer = [0]
    for i in string:
        if i in tmp:
            if answer[-1] == tmp[i]:
                answer.pop()
            else:
                return False
        else:
            answer.append(i)
    return len(answer) == 1

# 다른 사람의 풀이
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

if __name__ == '__main__':
    print(validBraces("()"), True);
    print(validBraces("[(])"), False);