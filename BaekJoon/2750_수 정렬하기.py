answer = []

# 삽입 정렬
# 정렬 범위를 1칸씩 확장해나가면서 새롭게 정렬 범위에 들어온 값을 기존값들과 비교하여
# 알맞은 자리에 꼽아주는 알고리즘
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

for i in range(int(input())):
    n = int(input())
    answer.append(n)

insertion_sort(answer)
# answer.sort()

for i in answer:
    print(i)

