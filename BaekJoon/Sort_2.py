answer = []

# 병합정렬(Merge Sort)
# 분할정복 알고리즘의 가장 좋은 예
# 정렬할 리스트를 반으로 나누어 두 부분을 따로 정렬하여 다시 조합하는 과정
def merge_sorted(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    l = merge_sorted(left)
    r = merge_sorted(right)
    return merge(l, r)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

for i in range(int(input())):
    n = int(input())
    answer.append(n)

answer = merge_sorted(answer)
# answer.sort()

for i in answer:
    print(i)

