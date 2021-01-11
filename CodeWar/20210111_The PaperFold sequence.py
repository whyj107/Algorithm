# The PaperFold sequence
# https://www.codewars.com/kata/5d26721d48430e0016914faa/train/python

# yield 가 뭘까?
# https://dojang.io/mod/page/view.php?id=2412

# 다른 사람의 풀이
def paper_fold():
    i = 1
    while True:
        yield not i & (i & -i) << 1
        i += 1

def paper_fold1():
    gen = paper_fold()
    while True:
        yield 1
        yield next(gen)
        yield 0
        yield next(gen)

print(paper_fold(), [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1])