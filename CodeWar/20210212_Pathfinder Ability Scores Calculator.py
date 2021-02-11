# Pathfinder Ability Scores Calculator
# https://www.codewars.com/kata/5df0041acec189002d06101f/train/python

# 나의 풀이
def pathfinder_scores(scores):
    cost = {7: -4, 8: -2, 9: -1, 10: 0, 11: 1, 12: 2,
            13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
    answer = []
    for score in scores:
        if score < 7 or score > 18:
            return False
        answer.append(cost[score])
    return sum(answer) <= 25

# 다른 사람의 풀이
PTS = dict(zip(range(7,19),(-4,-2,-1,0,1,2,3,5,7,10,13,17)))

def pathfinder_scores1(scores):
    return sum(PTS.get(x,float('inf')) for x in scores)<=25


print(pathfinder_scores([18, 13, 7, 12, 15, 10]), True)
print(pathfinder_scores([13, 12, 14, 12, 15, 11]), True)
print(pathfinder_scores([6, 19, 10, 10, 10, 10]), False)