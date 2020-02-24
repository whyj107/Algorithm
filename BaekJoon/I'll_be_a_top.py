for _ in range(int(input())):
    # 층 수 입력
    k = int(input())
    # 호실 수 입력
    n = int(input())

    #people에 1부터 호실+1까지의 수 넣기
    people = [i for i in range(1, n+1)]

    # 층 수 만큼 for문 실행
    for _ in range(k):
        # 호실 수 만큼 for문 실행
        for j in range(1, n):
            people[j] += people[j-1]

    print(people[-1])


