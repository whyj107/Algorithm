# 문제
# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

# 나의 풀이
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer

# 다른 사람의 풀이


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]), [4, 3, 1, 1, 0])