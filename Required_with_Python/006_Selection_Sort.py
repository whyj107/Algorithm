# 선택 정렬 알고리즘(Selection Sort Algorithm)
# 데이터의 처음부터 끝까지 훑어가면서 가장 작은 값을 찾은 후에 그 값을 첫 번째 데이터와 자리를 바꾸고,
# 그 다음에 두 번째로 작은 데이터를 찾아서 두 번째의 데이터와 자리를 바꾸는 방법
import random

def selection_sort(random_list):
    for sel in range(len(random_list)-1):
        min = random_list[sel]
        minindex = sel

        for step in range(sel + 1, len(random_list)):
            if min > random_list[step]:
                min = random_list[step]
                minindex = step

        random_list[minindex] = random_list[sel]
        random_list[sel] = min

if __name__=='__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1, 10))

    print("< Before Sort >")
    print(list)

    selection_sort(list)
    print("< After Sort >")
    print(list)