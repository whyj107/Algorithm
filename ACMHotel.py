for i in range(int(input())):
    h, w, n = map(int, input().split())
    answer_h = n % h
    answer_w = n // h + 1
    if answer_h == 0:
        answer_h = h
        answer_w -= 1
    print(answer_h*100+answer_w)