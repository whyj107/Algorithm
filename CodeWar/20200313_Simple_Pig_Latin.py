# 문제
# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word.
# Leave punctuation marks untouched.

# 입력 == 출력
# Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')

# --------------------------
# 내가 생각한 알고리즘대로 코드를 작성한 다음 한줄로 출력할 수 있도록 수정해 보았다.
# 한줄로 출력한게 더 간단한 것 같다
# --------------------------

# My Code
def pig_it(text):
    answer = []
    for i in text.split():
        if i.isalpha():
            answer.append(i[1:] + i[0] + 'ay')
        else:
            answer.append(i)
    # return ' '.join(answer)
    return ' '.join([i[1:] + i[0] + 'ay' if i.isalpha() else i for i in text.split()])

# Warriors Code
import re

def pig_it_(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)

if __name__=='__main__':
    answer = pig_it('Pig latin is cool')
    print(answer)
    answer = pig_it('Quis custodiet ipsos custodes ?')
    print(answer)
