def average_score(list):
    for i in range(5):
        score = int(input())
        if score < 40:
            score = 40
        list.append(score)
    return (int(sum(list)/len(list)))

def average_score1():
    sum = 0
    for i in range(5):
        score = int(input())
        if score < 40:
            score = 40
        sum += score
    return (sum//5)

if __name__=='__main__':
    score = []
    print(average_score(score))
    print(average_score1())