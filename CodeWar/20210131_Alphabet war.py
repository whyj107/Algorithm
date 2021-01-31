# Alphabet war
# https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python

# 나의 풀이
def alphabet_war(fight):
    left = 'sbpw'
    right = 'zdqm'
    l, r = 0, 0
    for f in fight:
        if f in left:
            l += (left.find(f)+1)
        elif f in right:
            r += (right.find(f)+1)
    if l > r:
        return 'Left side wins!'
    elif r > l:
        return 'Right side wins!'
    else:
        return "Let's fight again!"

# 다른 사람의 풀이
def alphabet_war1(fight):
    d = {'w': 4, 'p': 3, 'b': 2, 's': 1,
         'm': -4, 'q': -3, 'd': -2, 'z': -1}
    r = sum(d[c] for c in fight if c in d)

    return {r == 0: "Let's fight again!",
            r > 0: "Left side wins!",
            r < 0: "Right side wins!"
            }[True]

def alphabet_war2(fight):
    result = sum("zdqm".find(c) - "sbpw".find(c) for c in fight)
    return "{} side wins!".format("Left" if result < 0 else "Right") if result else "Let's fight again!"

print(alphabet_war("z"), "Right side wins!")
print(alphabet_war("zdqmwpbs"), "Let's fight again!")
print(alphabet_war("wq"), "Left side wins!")
print(alphabet_war("zzzzs"), "Right side wins!")
print(alphabet_war("wwwwww"), "Left side wins!")