x, y, w, h = map(int, input().split())

answer = []

# 1 <= x <= w-1
# 1 <= y <= h-1
answer.append(w - x)
answer.append(x - 0)
answer.append(h - y)
answer.append(y - 0)

print(min(answer))