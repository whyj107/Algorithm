# 문제
# Don't rely on luck
# The test fixture I use for this kata is pre-populated.
# It will compare your guess to a random number generated using:
# randint(1,100)
# You can pass by relying on luck or skill but try not to rely on luck.
# "The power to define the situation is the ultimate power." - Jerry Rubin
# Good luck!

# 입력 == 출력
# lucky_number = randint(1,100)
# test.assert_equals(guess, lucky_number, "Sorry. Unlucky this time.")

from random import randint, seed
seed(1)
guess = randint(1,100)
seed(1)
lucky_number = randint(1,100)
print(guess, lucky_number, "Sorry. Unlucky this time.")