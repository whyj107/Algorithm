# Max-min arrays
# https://www.codewars.com/kata/5a090c4e697598d0b9000004/train/python

# 나의 풀이
def solve(arr):
    answer = []
    arr.sort()
    cnt = -1
    while arr:
        answer.append(arr.pop(cnt))
        if cnt == -1: cnt = 0
        else: cnt = -1
    return answer

# 다른 사람의 풀이
def solve1(arr):
    lmax, lmin = iter(sorted(arr)) , iter(sorted(arr)[::-1])
    return [next(lmax) if i%2==1 else next(lmin) for i in range(0,len(arr))]

print(solve([15, 11, 10, 7, 12]), [15, 7, 12, 10, 11])
print(solve([91, 75, 86, 14, 82]), [91, 14, 86, 75, 82])
print(solve([84, 79, 76, 61, 78]), [84, 61, 79, 76, 78])
print(solve([52, 77, 72, 44, 74, 76, 40]), [77, 40, 76, 44, 74, 52, 72])
print(solve([1, 6, 9, 4, 3, 7, 8, 2]), [9, 1, 8, 2, 7, 3, 6, 4])
print(solve([78, 79, 52, 87, 16, 74, 31, 63, 80]), [87, 16, 80, 31, 79, 52, 78, 63, 74])