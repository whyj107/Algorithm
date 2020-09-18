# 문제
# Arrh, grabscrab!
# https://www.codewars.com/kata/52b305bec65ea40fe90007a7/train/python

# 나의 풀이
from collections import Counter
def grabscrab(word, possible_words):
    return [p for p in possible_words if Counter(word)==Counter(p)]

# 다른 사람의 풀이
def grabscrab(said, possible_words):
    return [ word for word in possible_words if sorted(word) == sorted(said) ]

print(grabscrab("trisf", ["first"]), ["first"])
print(grabscrab("oob", ["bob", "baobab"]), [])
print(grabscrab("ainstuomn", ["mountains", "hills", "mesa"]), ["mountains"])
print(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]), ["pool", "loop"])
print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]), ["sport", "ports"])
print(grabscrab("ourf", ["one","two","three"]), [])