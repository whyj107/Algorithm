# Simple directions reversal
# https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca/train/python

# 나의 풀이
def solve(arr):
    answer = []
    dic = {'Left': 'Right on ', 'Right': 'Left on ', '': 'Begin on '}
    pre = ''
    for i in range(len(arr)-1, -1, -1):
        tmp = arr[i].split(' on ')
        answer.append(dic[pre]+tmp[1])
        pre = tmp[0]
    return answer

# 다른 사람의 풀이
DIRS = {'Left': 'Right', 'Right': 'Left'}

def solve1(arr):
    lst, prevDir = [], 'Begin'
    for cmd in arr[::-1]:
        d, r    = cmd.split(' on ')
        follow  = DIRS.get(prevDir, prevDir)
        prevDir = d
        lst.append(f'{follow} on {r}')
    return lst

print(solve(['Begin on 3rd Blvd',
             'Right on First Road',
             'Left on 9th Dr']) == ['Begin on 9th Dr', 'Right on First Road', 'Left on 3rd Blvd'])
print(solve(["Begin on Road A", "Right on Road B", "Right on Road C", "Left on Road D"]) ==['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A'])
print(solve(["Begin on Road A"]) == ['Begin on Road A'])