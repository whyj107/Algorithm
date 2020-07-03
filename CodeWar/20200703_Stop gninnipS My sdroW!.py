# 문제
# Stop gninnipS My sdroW!
# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
# Examples:
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

# 입력 == 출력
# test.assert_equals(spin_words("Welcome"), "emocleW")

# My Code
def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) > 4 else i for i in sentence.split(' ')])

if __name__ == '__main__':
    print(spin_words("Welcome"), "emocleW")
    print(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
    print(spin_words("This is a test"), "This is a test")
    print(spin_words("This is another test"), "This is rehtona test")