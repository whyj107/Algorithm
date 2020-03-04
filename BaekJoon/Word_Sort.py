word = []

for i in range(int(input())):
    word.append(input())

# set을 사용하면 데이터의 중복을 허용하지 않음
set_word = list(set(word))

sort_word = []

# sort_word에 (글자수, 글자) 저장
for j in set_word:
    sort_word.append((len(j), j))

# 글자수로 1차 정렬하고 사전순으로 2차 정렬
sort_word.sort()

# sort_word에서 글자 출력
for len_word, word in sort_word:
    print(word)
