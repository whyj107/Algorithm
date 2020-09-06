# 문제
# 쇠막대기
# https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3

# 문제 풀이
def solution (arrangement):
    l = []
    answer = 0
    for i in arrangement:
        if i == "(":
            l.append(i)
            pre = i
        else:
            if pre == "(":
                l.pop()
                answer += len(l)
                pre = i
            else:
                l.pop()
                answer += 1

    return answer

if __name__ == "__main__":
    print(solution('(())'), 2)