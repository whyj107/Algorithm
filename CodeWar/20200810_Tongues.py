# 문제
# Tongues
# https://www.codewars.com/kata/52763db7cffbc6fe8c0007f8/train/python

# 나의 풀이
def tongues(code):
    s1 = 'aiyeoubkxznhdcwgpvjqtsrlmfAIYEOUBKXZNHDCWGPVJQTSRLMF'
    s2 = 'eouaiypvjqtsrlmfbkxznhdcwgEOUAIYPVJQTSRLMFBKXZNHDCWG'
    a = str.maketrans(s1, s2)
    return code.translate(a)

# 다른 사람의 풀이
def tongues1(code):
    import string
    gandalf = string.maketrans(
        'aiyeoubkxznhdcwgpvjqtsrlmfAIYEOUBKXZNHDCWGPVJQTSRLMF',
        'eouaiypvjqtsrlmfbkxznhdcwgEOUAIYPVJQTSRLMFBKXZNHDCWG')
    return string.translate(code, gandalf)

if __name__ == '__main__':
    print(tongues('Ita dotf ni dyca nsaw ecc.'), 'One ring to rule them all.')
    print(tongues('Tim oh nsa nowa gid ecc fiir wat ni liwa ni nsa eor ig nsaod liytndu.'),
                       'Now is the time for all good men to come to the aid of their country.')
    print(tongues('Giydhlida etr hakat uaedh efi iyd gidagensadh pdiyfsn ytni nsoh'),
                       'Fourscore and seven years ago our forefathers brought unto this')
    print(tongues('litnotatn e tam tenoit.'), 'continent a new nation.')
    print(tongues('Nsa zyolv pdimt gij xywbar ikad nsa cequ rifh.'),
                       'The quick brown fox jumped over the lazy dogs.')