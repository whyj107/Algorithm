# 문제
# 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3

# 나의 풀이
def solution(phone_number):
    return '*'*(len(phone_number)-4)+''.join(phone_number[-4:])

# 다른 사람의 풀이
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

if __name__ == '__main__':
    print(solution("01033334444"), "*******4444")