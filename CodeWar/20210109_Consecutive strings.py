# Consecutive strings
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

# 나의 풀이
def longest_consec(strarr, k):
    answer = [''.join(strarr[i:i+k]) for i in range(len(strarr))]
    answer.sort(key=len, reverse=True)
    return "" if strarr == [] or k < 1 or k > len(strarr) else answer[0]

# 다른 사람의 풀이
def longest_consec1(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""


print(longest_consec(['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 0) == "")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) == "oocccffuucccjjjkkkjyyyeehh")
print(longest_consec([], 3) == "")
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")