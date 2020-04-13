# 수난의 파사드 마방진

# 문제
# 이 마방진을 사용하여 다음 조건으로 덧셈한 결과 그 합이 같은 조합을 가장 많이 가지는 값(합)을 구해 보세요.
# 조건
# 서로 더할 수 있는 것은 가로, 세로, 대각선에 한정하지 않음
# 서로 더하는 수의 개수는 4개에 한정하지 않음

from itertools import combinations

# 마방진을 배열로 설정
magic_square = [1, 14, 14, 4, 11, 7, 6, 9,
                8, 10, 10, 5, 13, 2, 3, 15]

# 집계용 해시
memo = {}
for i in range(1, len(magic_square) + 1):
    # 조합 전체 탐색
    for comb in combinations(magic_square, i):
        # 조합 합계를 해시로 저장
        key = sum(comb)
        if key not in memo:
            memo[key] = 0
        memo[key] += 1

# 합계가 최대인 것을 출력
max_key = 0
max_value = 0
for key, value in memo.items():
    if max_value < value:
        max_key = key
        max_value = value
print("답 :", max_key)
print("조합 수 :", max_value)

# 2.-------------------------------------------
sum_all = sum(magic_square)
# 집계용 해시
ary = [0] * (sum_all + 1)

# 초깃값(아무것도 더하지 않을 때가 1개)
ary[0] = 1
for n in magic_square:
    # 큰 쪽부터 순서대로 가산
    for i in range(sum_all - n, - 1, - 1):
        ary[i + n] += ary[i]

# 합계가 최대인 것을 출력
print(ary.index(max(ary)))