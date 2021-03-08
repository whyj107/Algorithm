# Chuck Norris I - Push Ups
# https://www.codewars.com/kata/570564e838428f2eca001d73/train/python

# 나의 풀이
def chuck_push_ups(st):
    if type(st) != str or len(st) == 0: return 'FAIL!!'
    if st.count('1') == st.count('0') == 0: return "CHUCK SMASH!!"
    return max(int(''.join([j for j in i if j.isdecimal() and j < '2']), 2) for i in st.split() if i.count('1')>0 or i.count('0') > 0)

# 다른 사람의 풀이
from re import sub
def chuck_push_ups1(st):
    if st and isinstance(st, str):
        return max((int(x, 2) for x in sub(r"[^01\s]", "", st).split()), default="CHUCK SMASH!!")
    return "FAIL!!"

print(chuck_push_ups('1 "Chuck" 10 "Stop that!" 11 "Your vest looks stupid" 100 101 110'), 6)
print(chuck_push_ups('1000 "Did you kick someone in the face today?" 1001 1010 "Will I be making dinner then?!" 1011 110'), 11)
print(chuck_push_ups('10000 "Nice Beard" 1111 "Are you wearing denim shorts?" 1110 1101'), 16)
print(chuck_push_ups(''), 'FAIL!!')
print(chuck_push_ups([]), 'FAIL!!')
print(chuck_push_ups(1), 'FAIL!!')
print(chuck_push_ups("1ee1gf00t10h1011tr00"))