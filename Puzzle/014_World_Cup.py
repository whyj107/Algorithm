# 월드컵 출전국 끝말잇기

# 문제
# 각 나라를 한 번씩만 말할 수 있다고 할 때 가장 길게 이어지는 순서를 구하고 사용한 국가의 수를 답해 보세요.

country = ['Brazil', 'Croatia', 'Mexico', 'Cameroon',
           'Spain', 'Netherlands', 'Chile', 'Australia',
           'Colombia', 'Greece', "Cote d'Ivoire", 'Japan',
           'Uruguay', 'Costa Rica', 'England', 'Italy',
           'Switzerland', 'Ecuador', 'France', 'Honduras',
           'Argentina', 'Bosnia and Herzegovina', 'Iran',
           'Nigeria', 'Germany', 'Portugal', 'Ghana',
           'USA', 'Belgium', 'Algeria', 'Russia',
           'Korea Republic']

# 사용 완료 여부 확인
is_used = [False] * len(country)

def search(prev, depth):
    global max_depth
    is_last = True
    for i, c in enumerate(country):
        if c[0] == prev[-1].upper():
            if not is_used[i]:
                is_last = False
                is_used[i] = True
                search(c, depth + 1)
                is_used[i] = False
    if is_last:
        max_depth = max([max_depth, depth])
        return max_depth

# 모든 나라로부터 개시
max_depth = 0
for i, c in enumerate(country):
    is_used[i] = True
    search(c, 1)
    is_used[i] = False

# 깊이의 최대치(끝말잇기로 이어지는 나라의 수)를 표시
print(max_depth)