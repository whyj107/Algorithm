def star_9(n):
    tmp = 2*n-1
    space = 0
    for i in range(1, 2*n):
        print(' ' * space + '*' * tmp)
        if i < n:
            tmp -= 2
            space += 1
        else:
            tmp += 2
            space -= 1

if __name__=='__main__':
    star_9(int(input()))
