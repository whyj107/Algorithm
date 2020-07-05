# 문제
# The observed PIN
# Alright, detective, one of our colleagues successfully observed our target person,
# Robby the robber. We followed him to a secret warehouse,
# where we assume to find all the stolen stuff.
# The door to this warehouse is secured by an electronic combination lock.
# Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

# My Code
from itertools import product
def get_pins(observed):
    num = {'1': ["1", "2", "4"],      '2': ["2", "1", "3", "5"],      '3': ["3", "2", "6"],
           '4': ["4", "1", "5", "7"], '5': ["5", "2", "4", "6", "8"], '6': ["6", "3", "5", "9"],
           '7': ["7", "4", "8"],      '8': ["8", "5", "7", "9", "0"], '9': ["9", "6", "8"],
           '0': ["0", "8"]}
    return [''.join(i) for i in list(product(*[num[x] for x in observed]))]

# Warriors Code
ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')
def get_pins1(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]

if __name__ == '__main__':
    print(get_pins('8'), ['5', '7', '8', '9', '0'])
    print(get_pins('11'), ["11", "22", "44", "12", "21", "14", "41", "24", "42"])