def Star21(n):
    for i in range(2*n):
        for j in range(n):
            if i % 2 == 0:
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
            else:
                if j % 2 == 0:
                    print(' ', end='')
                else:
                    print('*', end='')
        print()

if __name__=='__main__':
    Star21(int(input()))
