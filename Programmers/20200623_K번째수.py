# 문제
# K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

# 나의 풀이
def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer

# 다름 사람의 풀이
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]), [5, 6, 3])