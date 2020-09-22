# 문제
# Breaking search bad
# https://www.codewars.com/kata/52cd53948d673a6e66000576/train/python

# 나의 풀이
def search(titles, term):
    return [t for t in titles if term in t.lower()]

# 다른 사람의 풀이
def search1(titles, term):
    return list(filter(lambda title: term in title.lower(), titles))

titles = ['The Big Bang Theory', 'How I Met Your Mother', 'Dexter', 'Breaking Bad', 'Doctor Who', 'The Hobbit', 'Pacific Rim', 'Pulp Fiction', 'The Avengers', 'Shining']
# print(search(titles, 'ho'), ['How I Met Your Mother', 'Doctor Who', 'The Hobbit'])
# print(search(titles, 'exte'), ['Dexter'])
print(search(titles, 'the'), ['The Big Bang Theory', 'How I Met Your Mother', 'The Hobbit', 'The Avengers'])

tmp = ['The Big Bang Theory', 'The Hobbit', 'The Avengers']
