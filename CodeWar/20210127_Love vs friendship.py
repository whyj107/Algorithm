# Love vs friendship
# https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python

# 나의 풀이
def words_to_marks(s):
    return sum(["abcdefghijklmnopqrstuvwxyz".find(i)+1 for i in s])

# 다른 사람의 풀이
def words_to_marks1(s):
  return sum(ord(c)-96 for c in s)

print(words_to_marks('attitude'), 100)
print(words_to_marks('friends'), 75)
print(words_to_marks('family'), 66)
print(words_to_marks('selfness'), 99)
print(words_to_marks('knowledge'), 96)