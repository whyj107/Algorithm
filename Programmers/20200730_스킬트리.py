# 문제
# 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3

# 나의 풀이
import re
def solution(skill, skill_trees):
    answer = 0
    p = '[^' + ''.join(skill) + ']+'
    for i in skill_trees:
        if re.match(p, i) != None and re.match(p, i).group() == i:
            answer += 1
        if not skill[0] in i:
            continue
        pre = -1
        for j in skill:
            if j in i and i.index(j) > pre:
                pre = i.index(j)
            elif j in i and i.index(j) < pre:
                break
            else:
                pre = 100
            if j == skill[-1]:
                answer += 1
    return answer

# 다른 사람의 풀이
def solution1(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution("CBD", ["CXF", "ASF", "BDF", "CEFD"]), 2)