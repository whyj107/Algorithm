from math import pi
# 반지름 입력 받기
r = int(input())

# 유클리드는 r의 제곱 곱하기 파이
euclid = r*r*pi
# 택시는 r의 제곱 곱하기 2
taxicab = r*r*2

print(round(euclid, 6))
print(round(taxicab, 6))
# 위의 포맷은 정수일 경우 소수점이 나오지 않음
# ---------------------------------
# 아래의 포맷이 더욱 정확
print("{0:.6f}".format(euclid))
print("{0:.6f}".format(taxicab))