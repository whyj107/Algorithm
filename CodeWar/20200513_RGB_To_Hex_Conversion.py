# 문제
# RGB To Hex Conversion
# The rgb function is incomplete.
# Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range must be rounded to the closest valid value.
#
# Note:
# Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

# 입력 == 출력
# test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
# test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
# test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
# test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
# test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")

# My Code
def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255

    if g < 0:
        g = 0
    elif g > 255:
        g = 255

    if b < 0:
        b = 0
    elif b > 255:
        b = 255

    return format(r, 'X').zfill(2) + format(g, 'X').zfill(2) + format(b, 'X').zfill(2)

def rgb1(r, g, b):
    return format(0 if r < 0 else 255 if r > 255 else r, 'X').zfill(2) \
           + format(0 if g < 0 else 255 if g > 255 else g, 'X').zfill(2) \
           + format(0 if b < 0 else 255 if b > 255 else b, 'X').zfill(2)

def rgb2(*rgb):
    return "".join([format(0 if i < 0 else 255 if i > 255 else i, 'X').zfill(2) for i in rgb])

# Warriors Code
def rgb3(r, g, b):
    clamp = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))

if __name__=='__main__':
    print(rgb2(0, 0, 0))
    print(rgb(1, 2, 3))
    print(rgb(255, 255, 255))
    print(rgb(254, 253, 252))
    print(rgb(-20, 275, 235))