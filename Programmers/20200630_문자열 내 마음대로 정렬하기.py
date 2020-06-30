# 문제
# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3

# 나의 풀이
def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    print(answer)
    return sorted(strings, key=lambda x: (x[n], x))

if __name__ == '__main__':
    print(solution(["sun", "bed", "car"], 1), ["car", "bed", "sun"])
    print(solution(["abce", "abcd", "cdx"], 2), ["abcd", "abce", "cdx"])