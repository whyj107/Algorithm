# 문제
# Not very secure

# 나의 풀이
import re
def alphanumeric(password):
    return re.compile('^[a-zA-Z0-9]+$').match(password) != None

# 다른 사람의 풀이
def alphanumeric1(string):
    return string.isalnum()

if __name__ == '__main__':
    print(alphanumeric("Passw0rd"), True)
    print(alphanumeric("hello world_"), False)