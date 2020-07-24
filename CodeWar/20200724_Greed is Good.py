# 문제
# Greed is Good

# 나의 풀이
def score(dice):
    answer = 0
    thr = {1: 1000, 6:600, 5: 500, 4:400, 3:300, 2: 200}
    one = {1:100, 5:50}
    for i in range(1, 7):
        tmp = dice.count(i)
        while tmp > 2:
            if tmp > 2 and i in thr:
                answer += thr[i]
                tmp -= 3
            else:
                break
        while tmp > 0:
            if tmp > 0 and i in one:
                answer += one[i]
                tmp -= 1
            else:
                break
    return answer

# 다른 사람의 풀이
def score1(dice):
    sum = 0
    counter = [0, 0, 0, 0, 0, 0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100, 0, 0, 0, 50, 0]
    for die in dice:
        counter[die - 1] += 1

    for (i, count) in enumerate(counter):
        sum += (points[i] if count >= 3 else 0) + extra[i] * (count % 3)

    return sum

if __name__ == '__main__':
    # print(score([2, 3, 4, 6, 2]), 0)
    print(score([4, 4, 4, 3, 3]), 400)
    print(score([2, 4, 4, 5, 4]), 450)
