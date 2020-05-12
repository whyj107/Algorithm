# 문제
# Opposite number
# Very simple, given a number, find its opposite.
#
# Examples:
# 1: -1
# 14: -14
# -34: 34

# 입력 == 출력
# test.assert_equals(opposite(1),-1)

# My Code
def opposite(number):
  return - number

def opposite1(number):
  return number * -1

if __name__=='__main__':
  print(opposite(1))
  print(opposite(-1))
  print(opposite(14))
  print(opposite(3))