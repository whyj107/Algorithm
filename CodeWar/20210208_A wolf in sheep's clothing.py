# A wolf in sheep's clothing
# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/python

# 나의 풀이
def warn_the_sheep(queue):
    return 'Pls go away and stop eating my sheep' if queue[-1] == 'wolf' else f"Oi! Sheep number {len(queue) - queue.index('wolf') - 1}! You are about to be eaten by a wolf!"

# 다른 사람의 풀이
def warn_the_sheep1(queue):
      n = len(queue) - queue.index('wolf') - 1
      return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'

print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']),
      'Oi! Sheep number 2! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']),
      'Oi! Sheep number 5! You are about to be eaten by a wolf!')
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']),
      'Oi! Sheep number 6! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'wolf', 'sheep']),
      'Oi! Sheep number 1! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'sheep', 'wolf']),
      'Pls go away and stop eating my sheep')