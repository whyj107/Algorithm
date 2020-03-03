# 문자열로 입력 받기
n = input()

# -----------------
# 문자열로 입력 받은 것을 list로 저장
# a = list(n)
# 문자열 list를 int형 list로 변환
# a = list(map(int, a))
# -----------------

# 위의 단계들을 한줄로 변형
answer = list(map(int, list(n)))

# answer.sort() 하면 오름차순 정렬
# 내림차순 정렬
answer.sort(reverse=True)

# list값들을 한개씩 출력
for n in answer:
    print(n, end="")