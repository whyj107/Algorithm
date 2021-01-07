# Tally it up
# https://www.codewars.com/kata/5630d1747935943168000013/train/python

# 나의 풀이
def score_to_tally(score):
    dic = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    answer = []
    idx = 5
    while score > 0:
        if score >= idx:
            score -= idx
            answer.append(dic[idx])
        else:
            idx -= 1
    return ' <br>'.join(answer) + (" <br>" if answer[-1] == 'e' else "")

# 다른 사람의 풀이
def score_to_tally1(s):
    return 'e <br>'*(s//5) + 'abcd'[s % 5 - 1:s % 5]

print(score_to_tally(3), 'c')
print(score_to_tally(10), 'e <br>e <br>')
print(score_to_tally(5), 'e <br>')
print(score_to_tally(1), 'a')
print(score_to_tally(16), 'e <br>e <br>e <br>a')
print(score_to_tally(28), 'e <br>e <br>e <br>e <br>e <br>c')
print(score_to_tally(19), 'e <br>e <br>e <br>d')
print(score_to_tally(9), 'e <br>d')
print(score_to_tally(15), 'e <br>e <br>e <br>')
print(score_to_tally(7), 'e <br>b')
