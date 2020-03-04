# 거품 정렬 알고리즘(Bubble Sort Algorithm)
# 순차적으로 바로 옆에 있는 데이터와 비교해서 옆의 데이터가 크면 자신과 위치를 변경
# 첫 번째 데이터가 가장 크다면 계속 옆에 있는 데이터와 자리를 바꾸면서 그 데이터는 결국 맨 끝으로 가게 된다.
# 두 변째 위치에 있는 데이터를 또다시 옆에 있는 데이터와 비교한다.
# 이와 같은 과정을 마지막의 바로 전 데이터까지 반복한다.
import random

compare_counter = 0
swap_counter = 0

def bubble_sort(random_list):
    for start_index in range(len(random_list)-1):
        for index in range(1, len(random_list) - start_index):
            if random_list[index - 1] > random_list[index]:
                temp = random_list[index-1]
                random_list[index - 1] = random_list[index]
                random_list[index] = temp

if __name__=='__main__':
    list = []
    input_n = input("정렬할 데이터의 수 : ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))
    print("< 정렬 전 >")
    print(list)

    bubble_sort(list)

    print("< 정렬 후 >")
    print(list)
