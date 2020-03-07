# 문제
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells
# and carries the "instructions" for the development and functioning of living organisms.
#
# If you want to know more http://en.wikipedia.org/wiki/DNA
#
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).
#
# More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

# 입력 == 출력
# Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
# Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
# Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")

# --------------------------
# 문자열 서로 교환
# A -> T
# T -> A
# C -> G
# G -> C

# string.maketrans()
# : 문자열을 치환해 주는 함수. 숫자가능. 단, 바꾸기 전/후 문자의 길이가 같아야 한다.
# --------------------------

# My Code
def DNA_strand(dna):
    answer = ""
    for i in dna:
        if i == 'A':
            answer += 'T'
        elif i == 'T':
            answer += 'A'
        elif i == 'C':
            answer += 'G'
        elif i == 'G':
            answer += 'C'

    return answer

# Warriors Code
def DNA_strand__(dna):
    pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join([pairs[x] for x in dna])

"""
아래와 같은 방법도 있다.
import string

def DNA_strand(dna):
    return dna.translate(string.maketrans('ATCG', 'TAGC'))
"""

if __name__=='__main__':
    answer = DNA_strand("ATTGC")  # return "TAACG"
    print(answer)
    answer = DNA_strand__("GTAT")  # return "CATA"
    print(answer)