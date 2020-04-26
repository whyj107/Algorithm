# 문제
# You will be given an array a and a value x.
# All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

# 입력 == 출력
# True, ([66, 101], 66)

# My Code
def check(seq, elem):
    return True if elem in seq else False

if __name__=='__main__':
    print(check([66, 101], 66))