# Figure Out the Notes
# https://www.codewars.com/kata/5602e85d255e3240c2000024/train/python

# 나의 풀이
def what_note(string, fret):
    code = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    return code[(code.index(string.upper()) + fret)%len(code)]

# 다른 사람의 풀이
# 박수를 보낸다 ㅋㅋㅋㅋㅋ
def what_note1(string, fret):
    return {
        'E': {0: 'E', 1: 'F', 2: 'F#', 3:'G', 4:'G#', 5:'A', 6:'A#', 7:'B', 8:'C', 9:'C#', 10:'D', 11:'D#', 12:'E'},
        'B': {0: 'B', 1: 'C', 2: 'C#', 3:'D', 4:'D#', 5:'E', 6:'F', 7:'F#', 8:'G', 9:'G#', 10:'A', 11:'A#', 12:'B'},
        'G': {0: 'G', 1: 'G#', 2: 'A', 3:'A#', 4:'B', 5:'C', 6:'C#', 7:'D', 8:'D#', 9:'E', 10:'F', 11:'F#', 12:'G'},
        'D': {0: 'D', 1: 'D#', 2: 'E', 3:'F', 4:'F#', 5:'G', 6:'G#', 7:'A', 8:'A#', 9:'B', 10:'C', 11:'C#', 12:'D'},
        'A': {0: 'A', 1: 'A#', 2: 'B', 3:'C', 4:'C#', 5:'D', 6:'D#', 7:'E', 8:'F', 9:'F#', 10:'G', 11:'G#', 12:'A'},
        'e': {0: 'E', 1: 'F', 2: 'F#', 3:'G', 4:'G#', 5:'A', 6:'A#', 7:'B', 8:'C', 9:'C#', 10:'D', 11:'D#', 12:'E'},
    }.get(string, {}).get(fret%12, '')

print(what_note("e", 0), "E")
print(what_note("D", 5), "G")
print(what_note("E", 18), "A#")
print(what_note("A", 1), "A#")
print(what_note("B", 8), "G")