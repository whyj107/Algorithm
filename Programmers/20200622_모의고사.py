# 문제
# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

# 나의 풀이
def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            cnt1 += 1
        if answers[i] == two[i % len(two)]:
            cnt2 += 1
        if answers[i] == thr[i % len(thr)]:
            cnt3 += 1

    if max(cnt1, cnt2, cnt3) == cnt1:
        answer.append(1)
    if max(cnt1, cnt2, cnt3) == cnt2:
        answer.append(2)
    if max(cnt1, cnt2, cnt3) == cnt3:
        answer.append(3)

    return answer

# 다른 사람의 풀이
def solution1(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]), [1])
    print(solution([1, 3, 2, 4, 2]), [1, 2, 3])