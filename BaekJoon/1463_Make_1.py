# 백준 1463 / 1로 만들기
def Make_1(N):
    lst = []
    for i in N:
        # 규칙 3
        lst.append(i - 1)
        # 규칙 1
        if i % 3 == 0:
            lst.append(i // 3)
        # 규칙 2
        if i % 2 == 0:
            lst.append(i // 2)
    # 중복 제거 후 리턴
    return list(set(lst))

if __name__=='__main__':
    # 입력 받기
    N = int(input())

    # 초기값 설정
    result = [N]
    cnt = 0

    # 1이 있을 때 까지 반복
    while True:
        # N이 1일 경우는 할 필요 없음
        if N == 1:
            break
        result = Make_1(result)
        cnt += 1
        if result.count(1) == 1:
            break
    # 출력
    print(cnt)