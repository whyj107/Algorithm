# Crack the PIN
# https://www.codewars.com/kata/5efae11e2d12df00331f91a6/train/python

# 나의 풀이
# hash 값은 돌려서 맞는 값밖에 찾지 못하므로
# for문을 이용해서 숫자를 hash 값으로 만든 뒤 비교해야 한다.
# zfill을 이용해서 자릿수를 맞춰준다.

import hashlib
def crack(hash):
    for i in range(100000):
        if hashlib.md5(str(i).zfill(5).encode()).hexdigest() == hash:
            return str(i).zfill(5)

print(crack("827ccb0eea8a706c4c34a16891f84e7b"), "12345")
print(crack("86aa400b65433b608a9db30070ec60cd"), "00078")