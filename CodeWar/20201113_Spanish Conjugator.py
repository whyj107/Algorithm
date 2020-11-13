# Spanish Conjugator
# https://www.codewars.com/kata/5a81b78d4a6b344638000183/train/python

# 나의 풀이
def conjugate(verb):
    dic = {"ar": ['o', 'as', 'a', 'amos', 'ais', 'an'],
           "er": ['o', 'es', 'e', 'emos', 'eis', 'en'],
           "ir": ['o', 'es', 'e', 'imos', 'is', 'en']}
    return {verb: [verb[:-2]+i for i in dic[verb[-2:]]]}

SUFFIXES = {'a': ['o', 'as', 'a', 'amos', 'ais', 'an'],
            'e': ['o', 'es', 'e', 'emos', 'eis', 'en'],
            'i': ['o', 'es', 'e', 'imos', 'is',  'en']}
def conjugate1(verb):
    return {verb: [verb[:-2] + s for s in SUFFIXES[verb[-2]]]}

print(conjugate("caminar") == {"caminar": ["camino", "caminas", "camina", "caminamos", "caminais", "caminan"]})
print(conjugate("comer") == {"comer": ["como", "comes", "come", "comemos", "comeis", "comen"]})
print(conjugate("vivir") == {"vivir": ["vivo", "vives", "vive", "vivimos", "vivis", "viven"]})
