# 배타적 논리합으로 만드는 삼각형

# 문제
#     1
#    1 1
#   1 0 1
#  1 1 1 1
# 1 0 0 0 1
# 위로부터 순서대로 배치해 나갈 때 2,014번쨰의 '0'이 출력되는 것은 몇 번째 단계인지 구해 보세요.

# '0'이 출현한 횟수
count = 0
# 현재의 행 수
line = 1
# 현재의 행의 값
row = [1]

while count < 2014:
    next_row = [1]
    # 앞의 행에서 배타적 논리합으로 다음 행을 설정
    for i in range(0, len(row) - 1):
        cell = row[i] ^ row[i + 1]
        next_row.append(cell)
        # '0'인 경우에 카운트
        if cell == 0:
            count += 1
    next_row.append(1)
    # 행 수를 늘려 다음의 행으로
    line += 1
    row = next_row

# 2,014개 카운트한 행을 출력
print(line)

# ---------------------------------
# '0'이 출현한 횟수
count = 0
# 현재의 행 수
line = 1
# 형재의 행의 값(비트열)
row = 1

while count < 2014:
    # 앞의 행에서 배타적 논리합으로 다음 행을 설정
    row ^= row << 1
    # '0'의 수를 카운트
    count += "{0:b}".format(row).count('0')
    line += 1

# 2,014개 카운트한 행을 출력
print(line)