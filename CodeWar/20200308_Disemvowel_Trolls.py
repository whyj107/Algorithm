# 문제
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove
# all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new
# string with all vowels removed.
# For example, the string "This website is for losers LOL!"
# would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

# 입력 == 출력
#test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

# --------------------------
# 모음이 지우기(a, e, i, o, u)
# 나는 vowel 리스트를 따로 만들었지만
# for r in 'aeiouAEIOU': 이렇게 사용 가능하다.
# 다른 사람들이 translate으로 문제를 풀었는데 내가 사용하는 버전에서는 오류가 난다.
# return string.translate(None, 'aeiouAEIOU')
# 그래서 내가 maketrans라는 것을 찾아서 수정해 줬다.
# --------------------------

# My Code
def disemvowel(string):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for r in vowel:
        string = string.replace(r, "")
    return string

# Warriors Code + My Code
def disemvowel_(s):
    return s.translate(str.maketrans({'a': '', 'e': '', 'i': '', 'o': '', 'u': '',
                                      'A': '', 'E': '', 'I': '', 'O': '', 'U': ''}))

if __name__=='__main__':
    s = disemvowel("This website is for losers LOL!")
    print(s)
    s = disemvowel_("This website is for losers LOL!")
    print(s)