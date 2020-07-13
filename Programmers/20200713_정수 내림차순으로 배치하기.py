# 문제
# 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3

# 나의 물이
def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))

def solution1(n):
    return int(''.join(sorted(str(n), reverse=True)))

if __name__ == '__main__':
  print(solution1(118372) == 873211)