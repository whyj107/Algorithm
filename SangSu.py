InputString = input()
tmp = InputString.split(' ')

if int(tmp[0][::-1]) > int(tmp[1][::-1]):
    print(tmp[0][::-1])
else:
    print(tmp[1][::-1])