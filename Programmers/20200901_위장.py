# 문제
# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

# 풀이
def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer [i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)

    print(cnt - 1)
    return '------------------'

from collections import Counter
from functools import reduce
def solution1(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

if __name__ == '__main__':
    print(solution1([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
                    ["green_turban", "headgear"], ["smoky_makeup", "face"]]), 11)
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"],
                   ["smoky_makeup", "face"]]), 3)