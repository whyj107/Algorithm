InputString = input()
CroatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in CroatiaAlphabet:
    InputString = InputString.replace(i, '*')
print(len(InputString))
