# 문제
# Ninja vs Samurai: Strike
# Something is wrong with our Warrior class.
# The strike method does not work correctly.
# The following shows an example of this code being used:
# ninja = Warrior('Ninja')
# samurai = Warrior('Samurai')
# samurai.strike(ninja, 3)
# ninja.health should == 70

# 입력 == 출력
# name=['Hattori Hanzo','Sasuke Sarutobi','Jubei Kibagami','Kotaro Fuma'][randint(0,3)]
# ninja = Warrior(name)
# Test.assert_equals(ninja.name,name,"Making the 'name' variable visible will help you complete this kata")

# My Code
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, enemy, swings):
        enemy.health = max([0, enemy.health - (swings * 10)])

from random import randint
if __name__ == '__main__':
    name = ['Hattori Hanzo', 'Sasuke Sarutobi', 'Jubei Kibagami', 'Kotaro Fuma'][randint(0,3)]
    ninja = Warrior(name)
    samurai = Warrior('Samurai')
    print(samurai.strike(ninja, 3))
