# 문제
# Convert a Number to a String!
# We need a function that can transform a number into a string.
# What ways of achieving this do you know?

# My Code
def number_to_string(num):
    return str(num)

def string_to_number(str):
    answer = 0
    cnt = 1
    for i in str[::-1]:
        if i == '-':
            answer *= -1
        else:
            answer += (int(i)*cnt)
        cnt *= 10
    return answer

if __name__ == '__main__':
    print(number_to_string(67) == '67')
    print(string_to_number('123'), 123)