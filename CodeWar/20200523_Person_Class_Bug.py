# 문제
# Person Class Bug
# The following code was thought to be working properly,
# however when the code tries to access the age of the person instance it fails.

# 입력 == 출력
# matz = Person('Yukihiro', 'Matsumoto', 47)
# Test.assert_equals(matz.full_name, 'Yukihiro Matsumoto')
# Test.assert_equals(matz.age, 47)
#
# joe = Person('Joe', 'Smith', 30)
# Test.assert_equals(joe.full_name, 'Joe Smith')
# Test.assert_equals(joe.age, 30)

# My Code
class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.age = age

if __name__ == '__main__':
    matz = Person('Yukihiro', 'Matsumoto', 47)
    print(matz.full_name, 'Yukihiro Matsumoto')
    print(matz.age, 47)

    joe = Person('Joe', 'Smith', 30)
    print(joe.full_name, 'Joe Smith')
    print(joe.age, 30)