# 입력 받기
N = int(input())

tmp = N

# 첫 번째 영화
movie = 666

while N:
    if "666" in str(movie):
        N -= 1

    movie += 1

print(movie - 1)

# 아래와 같이 하면 런타임 에러 발생
# 왜지....?
if (tmp - 1) == 0:
    print(666)
else:
    print(tmp-1, 666, sep='')

if __name__ == '__main__':
    print([i for i in range(9 ** 7) if "666" in str(i)][int(input()) - 1])