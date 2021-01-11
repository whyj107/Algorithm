# Fix my code
# https://www.codewars.com/kata/5b7bd90ef643c4df7400015d/train/python

# 회문 이용 : 앞 뒤가 똑같은 문자
# 각자 1씩 차이나는지 확인

# 나의 풀이
def solve(st):
    return all(ord(x) - ord(y) in [0, 2, -2] for x, y in zip(st, st[::-1]))

# 다른 사람의 풀이
def solve1(st):
    return all(abs(ord(x) - ord(y)) in {0, 2} for x, y in zip(st, st[::-1]))

print(solve("abba"), True)
print(solve("abaazaba"), False)
print(solve("abccba"), True)
print(solve("adfa"), True)
print(solve("ae"), False)
print(solve("abzy"), False)
print(solve("ababbaba"), True)
print(solve("sq"), True)
print(solve("kxbkwgyydkcbtjcosgikfdyhuuprubpwthgflucpyylbofvqxkkvqthmdnywpaunfihvupbwpruwfybdmgeuocltdaidyyewmbzm"),True)