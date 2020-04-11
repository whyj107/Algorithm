def padovan(N):
    padovan_list = [1] * N

    for i in range(3, N):
        padovan_list[i] = padovan_list[i-3] + padovan_list[i-2]

    return padovan_list[-1]

if __name__=='__main__':
    # T 입력 받기
    for i in range(int(input())):
        # N 입력 받기
        answer = padovan(int(input()))
        print(answer)