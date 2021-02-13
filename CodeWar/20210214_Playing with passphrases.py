# Playing with passphrases
# https://www.codewars.com/kata/559536379512a64472000053/train/python

# 다른 사람의 풀이
def play_pass(s, n):
    slower = s.lower()
    change = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i,char in list(enumerate(slower)):
        if char in alphabet:
            ind = (alphabet.index(char) + n)
            if ind >= 26:
                ind = ind % 26
            if i % 2 == 0:
                change += alphabet[ind].upper()
            else:
                change += alphabet[ind].lower()
        elif char.isdigit():
            change += str(9 - int(char))
        else:
            change += char

    return change[::-1]

def play_pass1(s, n):
    # Step 1, 2, 3
    shiftText = ""
    for char in s:
        if char.isdigit():
            shiftText += str(9 - int(char))
        elif char.isalpha():
            shifted = ord(char.lower()) + n
            shiftText += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
        else:
            shiftText += char

    # Step 4
    caseText = ""
    for i in range(len(shiftText)):
        caseText += shiftText[i].upper() if i % 2 == 0 else shiftText[i].lower()

    # Step 5
    return caseText[::-1]


print(play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")
print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2),
                   "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")