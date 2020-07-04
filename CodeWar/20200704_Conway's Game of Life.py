# 문제
# Conway's Game of Life
# The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
# At each step in time, the following transitions occur:
# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# My Code
def next_gen(cells):
    answer = []
    for i in range(len(cells)):
        tmp = []
        for j in range(len(cells[i])):
            cnt = fun1(i, j, cells)
            # cells[i][j]가 살아 있으면
            if cells[i][j] == 1 and cnt in [2, 3]:
                tmp.append(1)
            # cells[i][j]가 죽어 있으면
            elif cells[i][j] == 0 and cnt == 3:
                tmp.append(1)
            else:
                tmp.append(0)
        answer.append(tmp)
    return answer

def fun1(i, j, cells):
    cnt = 0
    for k in range(3):
        try:
            if i-1+k > -1:
                if cells[i-1+k][j-1] and j-1 > -1:
                    cnt += 1
                if cells[i-1+k][j]:
                    if k != 1:
                        cnt += 1
                if cells[i-1+k][j+1]:
                    cnt += 1
        except:
            pass
    return cnt

if __name__ == "__main__":
    print(next_gen([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), [[0, 0, 0], [1, 1, 1], [0, 0, 0]])