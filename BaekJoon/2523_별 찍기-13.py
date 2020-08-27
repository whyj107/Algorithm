def star_13(n):
    tmp = 1
    for i in range(1, 2*n):
        print('*' * tmp)
        if i < n:
            tmp += 1
        else:
            tmp -= 1

if __name__=='__main__':
    star_13(int(input()))