import math
a, b, v = map(int, input().split())
answer = (v-a)/(a-b)
print(math.ceil(answer))

#if answer == int(answer):
#    print(int(answer))
#else:
#    print(int(answer)+1)
