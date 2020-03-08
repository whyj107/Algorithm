# 날짜의 2진수 변환

# 문제
# 연월일을 YYYYMMDD의 8자리 정수로 나타내었을 때 2진수로 변환하여
# 거꾸로 나열한 다음 다시 10진수로 되돌렸을 때 원래 날짜와 같은 날짜가 되는 것을 찾아보세요.

# 1. YYYYMMDD의 포맷
# 2. 2진수로 변환
# 3. 2진수를 거꾸로 나열
# 4. 거꾸로 나열한 2진수를 10진수로 되돌림

# 날짜를 다루는 datetime 클래스 불러오기
from datetime import datetime, timedelta

# 기간 설정
start = datetime.strptime("1964-10-10", "%Y-%m-%d")
end = datetime.strptime("2020-07-24", "%Y-%m-%d")
step = timedelta(days=1)

# 해당하는 날짜 찾아 출력하기
while start <= end:
    day = bin(int(start.strftime("%Y%m%d"))).replace("0b", "")
    if day == day[::-1]:
        # print(bin(int(start.strftime("%Y%m%d"))).replace("0b", ""))
        print(start.strftime("%Y-%m-%d"))
    start += step

# ----------------------------------------------------------------------

# 대상 기간에서 2진수의 5번째 문자부터 8개의 문자 추출
from_left = int(bin(19641010).replace("0b", "")[4:4 + 8], 2)
to_left = int(bin(20200724).replace("0b", "")[4:4 + 8], 2)

# 좌우의 8문자를 반복
for i in range(from_left, to_left + 1):
    # 왼쪽
    l = "{0:08b}".format(i)
    # 오른쪽
    r = l[::-1]
    # 중앙
    for m in range(0, 1 + 1):
        value = "1001{}{}{}1001".format(l, m, r)
        try:
            # 변환 가능한지 확인
            date = datetime.strptime(str(int(value, 2)), "%Y%m%d")
            # 변환 가능할 경우 출력
            print(date.strftime("%Y-%m-%d"))
        except:
            pass