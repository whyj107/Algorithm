# 문제
# IP Validation
# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets,
# with values between 0 and 255, inclusive.
#
# Input to the function is guaranteed to be a single string.

# 입력 == 출력
# Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
# Test.assert_equals(is_valid_IP(''),                False)
# Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
# Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
# Test.assert_equals(is_valid_IP('12.34.56'),        False)
# Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
# Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
# Test.assert_equals(is_valid_IP('123.045.067.089'), False)
# Test.assert_equals(is_valid_IP('127.1.1.0'),        True)
# Test.assert_equals(is_valid_IP('0.0.0.0'),          True)
# Test.assert_equals(is_valid_IP('0.34.82.53'),       True)
# Test.assert_equals(is_valid_IP('192.168.1.300'),   False)

# My Code
def is_valid_IP(strng):
    try:
        ip_check = list(map(int, strng.split('.')))
        ip = strng.split('.')
        if len(ip) != 4:
            return False
        for i in range(len(ip)):
            if ip_check[i] < 0 or ip_check[i] > 255:
                return False
            if str(ip_check[i]) != ip[i]:
                return False
        return True
    except:
        return False

# Warriors Code
def is_valid_IP1(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4

if __name__=='__main__':
    print(is_valid_IP('12.255.56.1'))
    print(is_valid_IP(''))
    print(is_valid_IP('123.456.789.0'))
    print(is_valid_IP('123.045.067.089'))
    print(is_valid_IP('12.34.56 .1'))
    print(is_valid_IP('as.as.as.as'))
