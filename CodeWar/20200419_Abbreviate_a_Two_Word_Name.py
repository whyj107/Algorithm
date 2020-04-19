# 문제
# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# Patrick Feeney => P.F

# 입력 == 출력
# Test.assert_equals(abbrevName("Sam Harris"), "S.H");
# Test.assert_equals(abbrevName("Patrick Feenan"), "P.F");
# Test.assert_equals(abbrevName("Evan Cole"), "E.C");
# Test.assert_equals(abbrevName("P Favuzzi"), "P.F");
# Test.assert_equals(abbrevName("David Mendieta"), "D.M");

def abbrevName(name):
    return '.'.join([i[0].upper() for i in name.split(' ')])

if __name__=='__main__':
    answer = abbrevName("Sam Harris")
    print(answer)
    answer = abbrevName("Patrick Feenan")
    print(answer)
    answer = abbrevName("Evan Cole")
    print(answer)
    answer = abbrevName("P Favuzzi")
    print(answer)
    answer = abbrevName("David Mendieta")
    print(answer)