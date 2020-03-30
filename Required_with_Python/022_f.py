# 대리석 채우기
#   1.      2.      3.
#   ㅁ     ㅁㅁ    ㅁㅁ
#   ㅁ             ㅁㅁ
# 1번과 2번의 경우는 다 2개씩 있으면 3번과 같아진다.
# 그래서 1번과 2번은 f(n-2)이 된다.
# 3범의 경우는 f(n-1)

# 가로와 세로의 갯수를 n과 m으로 입력을 받아서 갯수를 구해보자.

def f(k, m):
    if k <= 1:
        return 1 % m
    else:
        return (f(k-1, m) + 2 * f(k-2, m)) % m

if __name__=='__main__':
    n = int(input("n : "))
    m = int(input("m : "))
    print(f(n, m))