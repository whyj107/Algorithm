# 문제
# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

# 나의 풀이
import math
def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    pre = 0
    for i in range(len(progresses)):
        if progresses[pre] < progresses[i]:
            answer.append(i-pre)
            pre = i
    answer.append(len(progresses)-pre)
    return answer

# 다른 사람의 풀이
def solution1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]), [2, 1])
    print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]), [1, 2, 3])