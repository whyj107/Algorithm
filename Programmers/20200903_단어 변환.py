# 문제
# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

# 나의 풀이
# 시간 초과가 있다.... 흠...
def solution0(begin, target, words):
    if not target in words: return 0
    queue = [begin]
    answer = 0
    while queue:
        n = queue.pop()
        for i in words:
            # 꼼수 부리다가 틀렸다.
            if len(set(n)-set(i)) == 1:
                queue.append(i)
        answer += 1
        if target in queue:
            return answer

def solution(begin, target, words):
    if not target in words: return 0
    queue = [begin]
    answer = 0
    while queue:
        n = queue.pop()
        for i in words:
            if sum(0 if x == y else 1 for x, y in zip(n, i)) == 1:
                queue.append(i)
        answer += 1
        if target in queue:
            return answer

if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)