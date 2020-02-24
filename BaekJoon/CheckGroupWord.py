cnt = 0
for i in range(int(input())):
    word = input()
    cnt += list(word) == sorted(word, key=word.find)
print(cnt)
##########################################################
case_num = int(input())
answer = []
for i in range(case_num):
    word = list(str(input()))
    for k in range(len(word)):
        if k!=len(word)-1 and word[k]==word[k+1]:
            pass
        elif word[k+1:].count(word[k]) != 0:
            break
        elif k==len(word)-1:
            answer.append(i)
print(len(answer))