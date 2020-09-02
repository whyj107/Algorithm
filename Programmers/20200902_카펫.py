# 문제
# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

# 나의 문제
def solution(brown, yellow):
    if (yellow + 2) * 3 - yellow == brown:
        return [yellow+2, 3]

    for i in range(yellow//2, 0, -1):
        if yellow%i == 0 and (i+2)*(yellow//i+2)-yellow==brown:
            return [i+2, yellow//i+2]

if __name__ == '__main__':
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))