# n번째의 카드부터 n-1장 간격으로 카드를 뒤집는 작업을 뒤집을 카드가 더는
# 없을 때까지 계속하라.
# 뒤집을 카드가 더는 없을 때 뒷변이 위를 향한 카드의 번호를 모두 구하라.

# 카드의 초기화
N = 100
cards = [False]*N

# 2~N까지 뒤집음
for i in range(2, N+1):
    j = i-1
    while j < len(cards):
        cards[j] = not cards[j]
        j += i

# 뒷면이 위를 향한 카드를 출력
for i in range(0, N):
    if not cards[i]:
        print(i+1)
