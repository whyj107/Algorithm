# 문제
# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3

# 나의 풀이
def solution0(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ""
        for j in range(n):
            if format(arr1[i], 'b').zfill(n)[j] == '0' and format(arr2[i], 'b').zfill(n)[j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)
    return answer

# 다른 사람의 풀이
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#').replace('0', ' ')
        answer.append(a12)
    return answer

if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]), ["#####","# # #", "### #", "# ##", "#####"])