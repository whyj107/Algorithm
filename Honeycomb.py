room = int(input())

if room == 1:
    answer = 1
else:
    num = 1
    answer = 1
    while room > 1:
        room -= num*6
        num += 1
        answer += 1

print(answer)