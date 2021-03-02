# Shifter words
# https://www.codewars.com/kata/603b2bb1c7646d000f900083/train/python

# 나의 풀이
def shifter(st):
    tmp = ["H", "I", "N", "O", "S", "X", "Z", "M", "W"]
    cnt = 0
    for i in list(set(st.split())):
        t = True
        for j in i:
            if not j in tmp:
                t = False
        if t:
            cnt += 1
    return cnt

# 다른 사람의 풀이
def shifter1(st):
    return sum(all(elem in "HIMNOSWXZ" for elem in x) for x in set(st.split()))

def shifter2(st):
    return sum(map(set("HINOSXZMW").__ge__, map(set, set(st.split()))))

print(shifter("ON"), 1)
print(shifter("OS IS UPDATED"), 2)
print(shifter("WHO IS WHO"), 2)
print(shifter("JS"), 0)
print(shifter("I III I III"), 2)
print(shifter(""), 0)