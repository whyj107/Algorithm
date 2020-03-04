# 셸 정렬 알고리즘(Shell SOrt Algorithm)
# 정렬할 데이터를 일정한 구간별로 쪼개서 그 구간 내에서 정렬을 한 후에 구간을 합쳐서 정렬

import random

def shell_sort(random_list):
    h = 1

    while h < len(random_list):
        h = h * 3 + 1

    h = h // 3

    while h > 0:
        for i in range(h):
            start_index = i + h

            while start_index < len(random_list):
                temp = random_list[start_index]
                insert_index = start_index

                while insert_index > h-1 and random_list[insert_index-h] > temp:
                    random_list[insert_index] = random_list[insert_index-h]
                    insert_index = insert_index - h

                random_list[insert_index] = temp
                start_index = start_index + h

        h = h//3

if __name__=='__main__':
    list = []
    input_n = input("정렬할 데이터의 수 : ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))

    print("< 정렬 전 >")
    print(list)

    shell_sort(list)

    print("< 정렬 후 >")
    print(list)
