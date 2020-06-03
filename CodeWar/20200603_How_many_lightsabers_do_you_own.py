# 문제
# How many lightsabers do you own?
# Inspired by the development team at Vooza,
# write the function howManyLightsabersDoYouOwn/how_many_light_sabers_do_you_own that
#
# accepts the name of a programmer, and
# returns the number of lightsabers owned by that person.
# The only person who owns lightsabers is Zach, by the way. He owns 18,
# which is an awesome number of lightsabers.
# Anyone else owns 0.

# 입력 == 출력
# test.assert_equals(how_many_light_sabers_do_you_own("Zach"), 18)
# test.assert_equals(how_many_light_sabers_do_you_own(), 0)
# test.assert_equals(how_many_light_sabers_do_you_own("zach"), 0)

# My Code
def how_many_light_sabers_do_you_own(name=''):
    return 18 if name == 'Zach' else 0

if __name__ == "__main__":
    print(how_many_light_sabers_do_you_own("Zach"), 18)
    print(how_many_light_sabers_do_you_own(), 0)
    print(how_many_light_sabers_do_you_own("zach"), 0)