# 문제
# Ninja vs Samurai: Attack + Block
# Something is wrong with our Warrior class.
# All variables should initialize properly and the attack method is not working as expected.
#
# If properly set, it should correctly calculate the damage after an attack
# (if the attacker position is == to the block position of the defender: no damage; otherwise,
# the defender gets 10 damage if hit "high" or 5 damage if hit "low".
# If no block is set, the defender takes 5 extra damage.

# 입력 == 출력
# Test.describe("First attack")
# ninja = Warrior('Hanzo Hattori')
# samurai = Warrior('Ryoma Sakamoto')
#
# samurai.block = 'l'
# ninja.attack(samurai, 'h')
# Test.it("Even the brave Ryoma Sakamoto was easily hit;
# in the full test we would better call the best japanese swordsman ever")
# Test.assert_equals(samurai.health, 90, 'Expected samurai health to equal 90, instead got ' + str(samurai.health))

# My Code
Position = {'high': 'h', 'low': 'l'}  # don't change this!

class Warrior():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.block = ""
        self.deceased = False
        self.zombie = False

    def attack(self, enemy, position):
        damage = 0
        if enemy.block != position:
            damage += 10 if position == Position['high'] else 5
        if enemy.block == "":
            damage += 5
        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):
        self.health = max(0, new_health)
        if self.deceased: self.zombie = True
        if self.health == 0:
            self.deceased = True
            self.zombie = False

if __name__ == '__main__':
    ninja = Warrior('Hanzo Hattori')
    samurai = Warrior('Ryoma Sakamoto')

    samurai.block = 'l'
    ninja.attack(samurai, 'h')

    print(samurai.health, 90)