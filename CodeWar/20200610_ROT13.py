# 문제
# How can you tell an extrovert from an introvert at NSA? Va gur ryringbef,
# gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
#
# I found this joke on USENET, but the punchline is scrambled.
# Maybe you can decipher it? According to Wikipedia, ROT13
# (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

# 입력 == 출력
# test.assert_equals(rot13("EBG13 rknzcyr."), "ROT13 example.")
# test.assert_equals(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."), "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
# test.assert_equals(rot13("123"), "123")
# test.assert_equals(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"), "This is actually the first kata I ever made. Thanks for finishing it! :)")
# test.assert_equals(rot13("@[`{"), "@[`{")

# My Code
def rot13(message):
    return ''.join([chr(ord(i)+13) if 'a'<=i<='m' or 'A'<=i<='M' else(chr(ord(i)-13) if 'n'<=i<='z' or 'N'<=i<='Z' else i) for i in message ])

# Warriors Code
def rot13_1(message):
    return message.encode('rot13')

if __name__ == '__main__':
    print(rot13('Hello'))