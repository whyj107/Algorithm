# 문제
# 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

# 나의 문제 풀이
def solution(s):
    return ' '.join([''.join(i[j].upper() if j%2 == 0 else i[j].lower() for j in range(len(i))) for i in s.split(' ')])

# 다른 사람의 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

if __name__ == '__main__':
    print(solution("try hello world"), "TrY HeLlO WoRlD")
