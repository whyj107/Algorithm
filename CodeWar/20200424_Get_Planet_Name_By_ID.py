# 문제
# The function is not returning the correct values.
# Can you figure out why?

# 입력 == 출력
# Test.assert_equals(get_planet_name(2), 'Venus')
# Test.assert_equals(get_planet_name(5), 'Jupiter')
# Test.assert_equals(get_planet_name(3), 'Earth')
# Test.assert_equals(get_planet_name(4), 'Mars')
# Test.assert_equals(get_planet_name(8), 'Neptune')
# Test.assert_equals(get_planet_name(1), 'Mercury')

# My Code
# 1. if와 elif 사용
def get_planet_name1(id):
    if id == 1:
        return 'Mercury'
    elif id == 2:
        return 'Venus'
    elif id == 3:
        return 'Earth'
    elif id == 4:
        return 'Mars'
    elif id == 5:
        return 'Jupiter'
    elif id == 6:
        return 'Saturn'
    elif id == 7:
        return 'Uranus'
    elif id == 8:
        return 'Neptune'

# 2. 배열 사용
def get_planet_name2(id):
    answer = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    return answer[id - 1]

# Warriors Code
def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)

if __name__=='__main__':
    print(get_planet_name1(2))
    print(get_planet_name2(5))
    print(get_planet_name1(3))
    print(get_planet_name2(4))
    print(get_planet_name1(8))
    print(get_planet_name2(1))