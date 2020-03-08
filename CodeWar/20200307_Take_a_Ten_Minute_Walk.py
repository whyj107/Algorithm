# 문제
# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends
# you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block in a direction and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives
# you will take you exactly ten minutes (you don't want to be early or late!) and will,
# of course, return you to your starting point. Return false otherwise.

# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).
# It will never give you an empty array (that's not a walk, that's standing still!).

# 입력 == 출력
# test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
# test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
# test.expect(not is_valid_walk(['w']), 'should return False');
# test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');

# --------------------------
# 10번만에 처음으로 돌아와라 이것이 포인트이다.
# 그래서 x와 y좌표 변수를 생성하여 이용하였다.
# + 길이가 10이 아니면 False 반환
# --------------------------

# My Code
def is_valid_walk(walk):
    x = 0
    y = 0

    if len(walk) != 8:
        return False

    for i in walk:
        if i is 'e':
            x += 1
        elif i is 'w':
            x -= 1
        elif i is 's':
            y += 1
        elif i is 'n':
            y -= 1

    if x == 0 and y == 0:
        return True
    else:
        return False

# Warriors Code
def isValidWalk_(walk):
    if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10:
       return True
    return False

if __name__=='__main__':
    bo = is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])
    print(bo)
    bo = isValidWalk_(['w','e','w','e','w','e','w','e','w','e','w','e'])
    print(bo)