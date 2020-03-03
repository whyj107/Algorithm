# 숫자 뒤집기
# 조건 01 : 정수의 자릿수를 계산 하는 방식을 고민해야 한다.
# 조건 02 : 이 문제의 경우는 반복문보다는 재귀 호출을 응용하는 것이 간단하다.
# Input : 1234
# Output : 4321

def solve(n):
    if n==0:
        return 0

    print(n%10, end=' ')
    solve(n//10)

if __name__=='__main__':
    num_str = input("입력 : ")
    num = int(num_str)
    solve(num)