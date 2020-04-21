# 회문(palindrome) 확인하기
# 회문 : 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말을 말한다.
# 조건 01 : 주어진 문자열의 처음과 끝의 문자를 비교하고 같으면 그 다음 문자를 비고하며,
#           아니면 빠져나온다.

str = "mississippi"
length = 11

def f():
    p = 0
    c = 0
    for i in range(length):
        j = i + 1
        while j < length:
            p = j - i + 1
            k = 0
            while i + k < j - k:
                if str[i + k] != str[j - k]:
                    p = 0
                    break
                k += 1
            c += p
            j += 1
    print("회문의 갯수: %d" % (c))

if __name__=='__main__':
    f()