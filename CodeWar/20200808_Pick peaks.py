# 문제
# Pick peaks
# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

# 나의 풀이
def pick_peaks(arr):
    answer = {"pos": [], "peaks": []}
    i = 1
    for idx in range(1, len(arr)-1):
        if arr[idx] == arr[idx+1]:
            continue
        if arr[i-1] < arr[idx] and arr[idx+1] < arr[idx]:
            answer["pos"].append(i)
            answer["peaks"].append(arr[i])
        i = idx+1
    return answer

# 다른 사람의 풀이
def pick_peaks1(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos': pos, 'peaks': [arr[i] for i in pos]}

if __name__ == '__main__':
    print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})
    print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {"pos": [3, 7], "peaks": [6, 3]})
    print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {"pos": [3, 7, 10], "peaks": [6, 3, 2]})
    print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {"pos": [2, 4], "peaks": [3, 2]})
    print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})
    print(pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]), {"pos": [2], "peaks": [3]})
    print(pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]), {"pos": [2], "peaks": [3]})
    print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]),
                       {"pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]})
    print(pick_peaks([]), {"pos": [], "peaks": []})
    print(pick_peaks([1, 1, 1, 1]), {"pos": [], "peaks": []})
    print(pick_peaks([20, 9, -4, 1, 9, 17, 2, 16, 9, 0, 4]), {'pos': [5, 7], 'peaks': [17, 16]})