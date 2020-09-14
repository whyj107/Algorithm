# 문제
# Sort Santa's Reindeer
# https://www.codewars.com/kata/52ab60b122e82a6375000bad/train/python

# 나의 풀이
def sort_reindeer(reindeer_names):
    tmp = [list(map(str, r.split(' '))) for r in reindeer_names ]
    tmp = sorted(tmp, key=lambda x: x[1])
    return [' '.join(i) for i in tmp]

# 다른 사람의 풀이
def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=lambda s:s.split()[1])

if __name__ == '__main__':
    print(sort_reindeer(['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada']),
                       ['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa'])
    print(sort_reindeer([]), [])
    print(sort_reindeer(
        ['Yasuo Kodai', 'Kenjiro Sado', 'Daisuke Aihara', 'Susumu Shima', 'Akira Sanada', 'Yoshikazu Okita',
         'Shiro Yabu', 'Sukeharu Nanbu', 'Sakezo Yamamoto', 'Hikozaemon Ohta', 'Juzo Mori', 'Saburo Tokugawa']),
                       ['Daisuke Aihara', 'Yasuo Kodai', 'Juzo Mori', 'Sukeharu Nanbu', 'Hikozaemon Ohta',
                        'Yoshikazu Okita', 'Kenjiro Sado', 'Akira Sanada', 'Susumu Shima', 'Saburo Tokugawa',
                        'Shiro Yabu', 'Sakezo Yamamoto'])
    print(sort_reindeer(['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']),
        ['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])
    print(sort_reindeer(["Sukeharu Yamamoto", "Juzo Yabu", "Saburo Shima", "Shiro Sanada", "Daisuke Mori"]),
        ['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])