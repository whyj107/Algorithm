# 문제
# Hamming Numbers

# 나의 풀이
def hamming(n):
    num = [1]
    i, j, k = 0, 0, 0
    if n == 1:
        return 1
    else:
        for _ in range(1, n):
            x = min(2*num[i], 3*num[j], 5*num[k])
            num.append(x)
            if 2*num[i] <= x: i += 1
            if 3*num[j] <= x: j += 1
            if 5*num[k] <= x: k += 1
        return num[len(num) - 1]

# 다른 사람의 풀이
def hamming1(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

def hamming2(n):
    bag = {1}
    for _ in range(n - 1):
        head = min(bag)
        bag.remove(head)
        bag |= {head*2, head*3, head*5}
    return min(bag)

if __name__ == '__main__':
    # print(hamming(1) == 1);
    # print(hamming(2) == 2);
    # print(hamming(3) == 3);
    # print(hamming(4), 4);
    # print(hamming(5), 5);
    print(hamming(6), 6);
    print(hamming(7), 8);
    print(hamming(8), 9);
    print(hamming(9), 10);
    print(hamming(10), 12);
    print(hamming(11), 15);
    print(hamming(12), 16);
    print(hamming(13), 18);
    print(hamming(14), 20);
    print(hamming(15), 24);
    print(hamming(16), 25);
    print(hamming(17), 27);
    print(hamming(18), 30);
    print(hamming(19), 32);