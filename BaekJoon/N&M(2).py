import sys

def testCase():
    input_val = list(map(int, sys.stdin.readline().split()))
    global N, M
    N, M = input_val

def solve(remain, result=[]):
    if len(result) == M:
        for r in result:
            print(r, end=' ')
        print()
        return

    for idx in range(len(remain)):
        result.append(remain[idx])
        solve(remain[idx+1:], result)
        result.pop(-1)

if __name__=='__main__':
    testCase()
    solve(range(1, N+1))