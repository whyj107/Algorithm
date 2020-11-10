# Fix string case
# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

# 나의 풀이
def solve0(s):
    cnt1, cnt2 = 0, 0
    for i in s:
        if i.islower():
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= cnt2:
        return s.lower()
    else:
        return s.upper()

def solve(s):
    cnt1 = sum([1 for i in s if i.islower()])
    cnt2 = sum([1 for i in s if i.isupper()])
    return s.lower() if cnt1 >= cnt2 else s.upper()

# 다른 사람의 풀이
def solve1(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()

print(solve("code") == "code")
print(solve("CODe") == "CODE")
print(solve("COde") == "code")
print(solve("Code") == "code")
