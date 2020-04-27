# 백준 2156 포도주 시식
def solve(wine):
    # 점화식 과정을 담을 list 생성
    answer = [0 for _ in range(len(wine))]
    # index 1의 초기값을 입력 받은 리스트 값의 0으로 설정
    answer[0] = wine[0]
    # 입력 받은 리스트의 길이가 1개이면 answer[1] 반환
    if len(wine) < 2:
        return answer[0]
    # index 2의 초기값을 입력 받은 리스트 0과 1의 합으로 설정
    answer[1] = wine[0] + wine[1]
    # 입력 받은 리스트의 길이가 2이면 answer[2] 반환
    if len(wine) < 3:
        return answer[1]
    # 입력 받은 리스트의 길이가 3이상이면 answer의 마지막 값을 반환
    for i in range(2, len(wine)):
        answer[i] = max(answer[i - 1],
                        answer[i - 2] + wine[i],
                        answer[i - 3] + wine[i - 1] + wine[i])
    # 마지막 값 반환
    return answer[-1]

if __name__=='__main__':
    wine = []
    for i in range(int(input())):
        wine.append(int(input()))
    print(solve(wine))