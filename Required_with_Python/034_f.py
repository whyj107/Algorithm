# 3x3 행렬 중 합이 최소가 되는 항목 선택하기
# 조건 01 : 파이썬에서 제공하는 최댓값 상수를 이용한다.
# 조건 02 : 백트래킹 기반의 재귀 함수를 이용한다.
# 조건 03 : 한 번 선택한 항목을 다시 선택하지 않도록 하기 위해 별도의 플래그 배열을 사용한다.

INT_MAX = 10000
m = [[1, 5, 3], [2, 5, 7], [5, 3, 5]]
col_check = [False, False, False]
min_sol = INT_MAX

def f(row, score):
    global min_sol

    if row == 3:
        if score < min_sol:
            min_sol = score
        return min_sol

    for i in range(3):
        if col_check[i] == False:
            col_check[i] = True
            f(row + 1, score + m[row][i])
            col_check[i] = False

    return min_sol

if __name__=='__main__':
    print('min_sol : %d' % f(0, 0))