# 문제
# My smallest code interpreter (aka Brainf**k)

# Warriors Code
from collections import defaultdict

def brain_luck(code, input):
    p, i = 0, 0
    output = []
    input = iter(input)
    data = defaultdict(int)
    while i < len(code):
        c = code[i]
        if c == '+': data[p] = (data[p] + 1) % 256
        elif c == '-': data[p] = (data[p] - 1) % 256
        elif c == '>': p += 1
        elif c == '<': p -= 1
        elif c == '.': output.append(chr(data[p]))
        elif c == ',': data[p] = ord(next(input))
        elif c == '[':
            if not data[p]:
                depth = 1
                while depth > 0:
                    i += 1
                    c = code[i]
                    if c == '[': depth += 1
                    elif c== ']': depth -= 1
        elif c == ']':
            if data[p]:
                depth = 1
                while depth > 0:
                    i -= 1
                    c = code[i]
                    if c == ']': depth += 1
                    elif c == '[': depth -= 1
        i += 1
    return ''.join(output)

if __name__ == '__main__':
    # Echo until byte(255) encountered
    print(
        brain_luck(',+[-.,+]', 'Codewars' + chr(255)),
        'Codewars'
    )

    # Echo until byte(0) encountered
    print(
        brain_luck(',[.[-],]', 'Codewars' + chr(0)),
        'Codewars'
    )

    # Two numbers multiplier
    print(
        brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)),
        chr(72)
    )