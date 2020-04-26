# 문제
# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
# Your task is to change the letters with diacritics:
# ą -> a,
# ć -> c,
# ę -> e,
# ł -> l,
# ń -> n,
# ó -> o,
# ś -> s,
# ź -> z,
# ż -> z
# and print out the string without the use of the Polish letters.

# 입력 == 출력
# test.assert_equals(correct_polish_letters("Jędrzej Błądziński"),"Jedrzej Bladzinski");
# test.assert_equals(correct_polish_letters("Lech Wałęsa"),"Lech Walesa");
# test.assert_equals(correct_polish_letters("Maria Skłodowska-Curie"),"Maria Sklodowska-Curie")

# My Code
def correct_polish_letters(st):
    return st.replace('ą', 'a').replace('ć', 'c').replace('ę', 'e')\
        .replace('ł', 'l').replace('ń', 'n').replace('ó', 'o').\
        replace('ś', 's').replace('ź', 'z').replace('ż', 'z')

if __name__=='__main__':
    print(correct_polish_letters("Jędrzej Błądziński"))