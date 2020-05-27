# 문제
# Make the Deadfish swim
# Write a simple parser that will parse and run Deadfish.
#
# Deadfish has 4 commands, each 1 character long:
#
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# 입력 == 출력
# Test.assert_equals(parse("ooo"), [0,0,0])
# Test.assert_equals(parse("ioioio"), [1,2,3])
# Test.assert_equals(parse("idoiido"), [0,1])
# Test.assert_equals(parse("isoisoiso"), [1,4,25])
# Test.assert_equals(parse("codewars"), [0])

# My Code
def parse(data):
    answer = []
    answer_tmp = 0
    for i in data:
        if i == "i":
            answer_tmp += 1
        elif i == "d":
            answer_tmp -= 1
        elif i == "s":
            answer_tmp *= answer_tmp
        elif i == "o":
            answer.append(answer_tmp)
    return answer

if __name__ == '__main__':
    print(parse("ooo"), [0, 0, 0])
    print(parse("ioioio"), [1, 2, 3])
    print(parse("idoiido"), [0, 1])
    print(parse("isoisoiso"), [1, 4, 25])
    print(parse("codewars"), [0])
