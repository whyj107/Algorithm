# Backspaces in string
# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python

# 나의 풀이
def clean_string(s):
    answer = []
    for i in s:
        if i == '#':
            try:
                answer.pop()
            except:
                pass
        else:
            answer.append(i)
    return ''.join(answer)

# 다른 사람의 풀이
def clean_string1(s):
    stk = []
    for c in s:
        if c=='#' and stk: stk.pop()
        elif c!='#':       stk.append(c)
    return ''.join(stk)

print(clean_string('abc#d##c'), "ac")
print(clean_string('abc####d##c#'), "" )
print(clean_string("#######"), "" )
print(clean_string(""), "" )
