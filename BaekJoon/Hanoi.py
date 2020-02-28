def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else:
        hanoi(disk - 1, start, end, mid)
        print(start, end)
        hanoi(disk - 1, mid, start, end)

total = int(input())
answer = 0

for disk in range(total):
    answer = answer*2
    answer += 1

print(answer)
hanoi(total, 1, 2, 3)