InputString = input()
if InputString is ' ':
    print(0)
else:
    answer = InputString.split(' ')
    for i in range(answer.count('')):
        answer.remove('')
    print(len(answer))

