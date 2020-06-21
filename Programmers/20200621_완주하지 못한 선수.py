# 문제
# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

# 나의 풀이
# 1. 효율성 테스트 실패
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    return ''.join(participant)

# 2. 효율성 테스트 성공
from collections import Counter
def solution1(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    p.subtract(c)
    return p.most_common(1)[0][0]

# 다른 사람의 풀이
def solution2(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

if __name__ == '__main__':
    print(solution1([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5]))
    print(solution1(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))