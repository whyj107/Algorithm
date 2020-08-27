def solve(list):
    # answer라는 리스트 생성
    answer = [0 for _ in range(len(list))]
    # 0-2까지 인덱스에 미리 초기값을 설정
    answer[0] = list[0]

    # list 길이가 2보다 작을 경우는 answer[0]값을 리턴
    if len(list) < 2:
        return answer[0]

    answer[1] = list[0] + list[1]

    # list 길이가 3보다 작을 경우는 answer[1]값을 리턴
    if len(list) < 3:
        return answer[1]

    answer[2] = max(list[1] + list[2], list[0] + list[2])
    # 3부터 나머지 길이 만큼 반복
    for i in range(3, len(list)):
        # 2가지 경우의 수중 큰 수를 answer 리스트에 저장
        answer[i] = max(answer[i - 3] + list[i - 1] + list[i], answer[i - 2] + list[i])
    # 맨 마지막 값 외에는 문제 풀이를 위한 값이므로 마지막 값 리턴
    return answer[-1]

if __name__=='__main__':
    input_list = []
    # 입력 받기
    for i in range(int(input())):
        input_list.append(int(input()))

    answer = solve(input_list)
    # 출력
    print(answer)