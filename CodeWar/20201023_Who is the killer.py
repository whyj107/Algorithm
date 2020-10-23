# Who is the killer?
# https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d/train/python

# 나의 풀이
def killer(suspect_info, dead):
    for k in suspect_info.keys():
        cnt = 0
        for d in dead:
            if d in suspect_info[k]:
                cnt += 1
        if cnt == len(dead):
            return k

# 다른 사람의 풀이
def killer1(suspect_info, dead):
    is_killer = set(dead).issubset
    return next(k for k, L in suspect_info.items() if is_killer(L))

"""
isdisjoint() : 두 집합이 공통 원수인가(true/false)
issubset() : 부분 집합인가
issuperset() : 확대 집합인가
"""


print(killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']),
      'James')
print(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']), 'Megan')