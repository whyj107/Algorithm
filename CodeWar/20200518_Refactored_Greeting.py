# 문제
# Refactored Greeting
# The following code could use a bit of object oriented artistry.
# While its a simple method and works just fine as it is,
# in a larger system its best to organize methods into classes/objects.
# Refactor the following code so that it belongs to a Person class/object.
# Each Person instance will have a greet method.
# The Person instance should be instantiated with a name
# so that it no longer has to be passed into each greet method call.

# 입력 == 출력
# Test.assert_equals(jack.greet("Jill"), "Hello Jill, my name is Jack")
# Test.assert_equals(jack.greet("Mary"), "Hello Mary, my name is Jack")
#
# Test.assert_equals(jill.greet("Jack"), "Hello Jack, my name is Jill")
# Test.assert_equals(jill.name, 'Jill', "Person's name could not be retrieved")

# My Code
class Person:
    def __init__(self, my_name):
        self.name = my_name

    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)

# Warriors Code
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other):
        return f"Hello {other}, my name is {self.name}"

if __name__=='__main__':
    jack = Person("Jack")
    print(jack.greet("Jill"))