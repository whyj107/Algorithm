# 삽입 정렬 알고리즘(Insert Sort Algorithm)
# 순차적으로 정렬하면서 현재의 값을 정렬되어 있는 값들과 비교하여 위치로 삽입하는 방식

import random

def insertion_sort(my_list):
    my_list.insert(0, -1)
    for s_idx in range(2, len(my_list)):
        temp = my_list[s_idx]
        ins_idx = s_idx
        while my_list[ins_idx - 1] > temp:
            my_list[ins_idx] = my_list[ins_idx - 1]
            ins_idx = ins_idx - 1

        my_list[ins_idx] = temp

    del my_list[0]

if __name__=='__main__':
    list = []
    input_n = input("정렬할 데이터의 수 : ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))

    print("< 정렬 전 >")
    print(list)

    insertion_sort(list)

    print("< 정렬 후 >")
    print(list)
