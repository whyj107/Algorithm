import math
A, B, C = map(int, input().split())
answer = 0
# answer => A/(C-B)
if B<C:
    answer = A/(C-B)
    if answer == math.ceil(answer):
        print(int(answer+1))
    else:
        print(math.ceil(answer))
else:
    print(-1)