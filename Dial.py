InputString = input()
answer = 0
for i in range(len(InputString)):
    if InputString[i] <= 'C':
        answer = answer+3
    elif InputString[i] <= 'F':
        answer = answer+4
    elif InputString[i] <= 'I':
        answer = answer+5
    elif InputString[i] <= 'L':
        answer = answer+6
    elif InputString[i] <= 'O':
        answer = answer+7
    elif InputString[i] <= 'S':
        answer = answer+8
    elif InputString[i] <= 'V':
        answer = answer+9
    elif InputString[i] <= 'Z':
        answer = answer+10
    else:
        answer = answer+11
print(answer)

print(sum(min(ord(c)-64, 25)*28//89+3for c in input()))

for i in InputString:
    print(i)