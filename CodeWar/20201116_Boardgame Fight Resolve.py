# Boardgame Fight Resolve
# https://www.codewars.com/kata/58558673b6b0e5a16b000028/train/python

# 나의 풀이
def fight_resolve(defender, attacker):
    if (defender.isupper() and attacker.isupper()) or (defender.islower() and attacker.islower()): return -1
    defen_win = {"k": ["A", "a"], "s": ["P", "p"], "a": ["S", "s"], "p": ["K", "k"]}
    return defender if attacker in defen_win[defender.lower()] else attacker

# 다른 사람의 풀이
def fight_resolve1(d, a):
    return -1 if d.islower() == a.islower() else d if d.lower() + a.lower() in "ka sp as pk" else a

print(fight_resolve('K', 'A'), -1)
print(fight_resolve('S', 'A'), -1)
print(fight_resolve('k', 's'), -1)
print(fight_resolve('a', 'a'), -1)
print(fight_resolve('k', 'A'), 'k')
print(fight_resolve('K', 'a'), 'K')