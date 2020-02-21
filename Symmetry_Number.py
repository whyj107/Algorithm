# 앞뒤가 같은 10진수 만들기
# 문제 : 10진수, 2진수, 8진수 그 어느 것으로 표현하여도 대칭수가 되는 수 중,
# 10진수의 10 이상에서의 최솟값을 구하라

# 11부터 탐색 개시
num = 11

while True:
    # 진법에 따른 변수를 선언
    num_10 = str(num)
    num_8 = oct(num).replace("0o", "")
    num_2 = bin(num).replace("0b", "")

    # 앞뒤가 같은지 확인
    if num_10 == num_10[::-1] and num_8 == num_8[::-1] and num_2 == num_2[::-1]:
        print(num)
        break

    # 홀수만 탐색하므로 2씩 늘림
    num += 2
