def select_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0

if __name__=='__main__':
    x = int(input())
    y = int(input())
    answer = select_quadrant(x, y)
    print(answer)