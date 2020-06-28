# 문제
# Palindrome chain length
# Number is a palindrome if it is equal to the number with digits in reversed order.
# For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.
# Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to obtain a palindrome. The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome,
# repeat the procedure with the sum until the resulting number is a palindrome.
# If the input number is already a palindrome, the number of steps is 0.
# Input will always be a positive integer.
# For example, start with 87:
# 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884
# 4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4

# 입력 == 출력
# test.assert_equals(palindrome_chain_length(87), 4)

# My Code
def palindrome_chain_length(n):
    answer = []
    pal = int(str(n)[::-1])
    while n != pal:
        n += pal
        pal = int(str(n)[::-1])
        answer.append(n)
    return len(answer)

# Warriors Code
def palindrome_chain_length1(n):
    steps = 0
    while str(n) != str(n)[::-1]:
        n = n + int(str(n)[::-1])
        steps += 1
    return steps

if __name__ == '__main__':
    print(palindrome_chain_length(87), 4)