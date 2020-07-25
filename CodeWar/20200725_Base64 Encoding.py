# 문제
# Base64 Encoding
# https://www.codewars.com/kata/5270f22f862516c686000161/train/python

# 문제의 특징이 Incorrect Padding은 무시하면서,
# '='이 끝에 붙지 않도록 하는 것이다.
# 하지만, 현재 나의 문제 풀이로는 '='이 끝에 붙어서 나오게 된다.
# 나의 풀이
import base64
def to_base_64(string):
    return base64.b64encode(string.encode('ascii')).decode('ascii')

def from_base_64(string):
    return base64.b64decode(string).decode('ascii')

# 다른 사람의 풀이
def to_base_64_1(string):
    return base64.b64encode(string.encode('ascii')).decode('ascii').replace("=","")

def from_base_64_1(string):
    return base64.b64decode(string.encode('ascii')+b'===').decode('ascii').replace("=","")

if __name__ == '__main__':
    # print(from_base_64('6zqYkdcYWI+FZH'), 'NnpxWWtkY1lXSStGWkg')

    tests = [["this is a string!!", "dGhpcyBpcyBhIHN0cmluZyEh"],
             ["this is a test!", "dGhpcyBpcyBhIHRlc3Qh"],
             ["now is the time for all good men to come to the aid of their country.",
              "bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
             ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
             ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
             ["the quick brown fox jumps over the white fence. ",
              "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
             ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4",
              "ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
             ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna", "VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
             ["TVRJek5EVTJOemc1TUNBZyAg", "VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]]

    for test in tests:
        result = to_base_64(test[0])
        print(result, test[1])
        print(from_base_64(result), test[0])