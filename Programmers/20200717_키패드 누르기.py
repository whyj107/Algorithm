# 문제
# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

# 나의 풀이
def solution(numbers, hand):
    answer = ''
    l, r = '*', '#'
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            l = i
        elif i in [3, 6, 9]:
            answer += "R"
            r = i
        elif i in [2, 5, 8, 0]:
            l_cnt, r_cnt = 0, 0

            if l in [2, 5, 8, 0]:
                l_cnt = abs([2, 5, 8, 0].index(i) - [2, 5, 8, 0].index(l))
            else:
                l_cnt = abs([2, 5, 8, 0].index(i) - [1, 4, 7, '*'].index(l))+1
            if r in [2, 5, 8, 0]:
                r_cnt = abs([2, 5, 8, 0].index(i) - [2, 5, 8, 0].index(r))
            else:
                r_cnt += abs([2, 5, 8, 0].index(i) - [3, 6, 9, '#'].index(r))+1

            if l_cnt < r_cnt:
                answer += 'L'
                l = i
            elif l_cnt == r_cnt:
                answer += hand[0].upper()
                if hand[0].upper() == 'L':
                    l = i
                else:
                    r = i
            else:
                answer += 'R'
                r = i
    return answer

if __name__ == '__main__':
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")