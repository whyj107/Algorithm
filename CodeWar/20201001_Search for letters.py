# 문제
# Search for letters
# https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python

# 나의 풀이
def change(st):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ["0"]*26
    for i in st:
        if i.lower() in alpha:
            answer[alpha.index(i.lower())] = "1"
    return ''.join(answer)


print(change("a **&  bZ"), "11000000000000000000000001")
print(change('Abc e  $$  z'), "11101000000000000000000001")
print(change("!!a$%&RgTT"), "10000010000000000101000000")
print(change(""), "00000000000000000000000000")
print(change("abcdefghijklmnopqrstuvwxyz"), "11111111111111111111111111")
print(change("aaaaaaaaaaa"), "10000000000000000000000000")
print(change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd"), "00010111000000000001000010")