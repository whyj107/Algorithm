# 문제
# Grab CSV Columns
# https://www.codewars.com/kata/5276c0f3f4bfbd5aae0001ad/train/python

# 나의 풀이
def csv_columns(csv, indices):
    tmp = [i.split(',') for i in csv.split('\n')]
    answer = []
    for i in tmp:
        a = []
        for j in sorted(set(indices)):
            if len(i) > j:
               a.append(i[j])
        if not len(a) < 1:
            answer.append(','.join(a))
    return '\n'.join(answer) if not len(answer) < 1 else ''

# 다른 사람의 풀이
def csv_columns(csv, indices):
    indices = sorted(set(indices))
    lines = csv.splitlines()

    result = []

    for line in lines:
        values = line.split(',')
        result.append(','.join(values[i] for i in indices if i < len(values)))

    return '\n'.join(result).strip()

if __name__ == '__main__':
    print(csv_columns("1,2\n3,4\n5,6", [5, 6, 7]) == "")
    print(csv_columns("1,2,3\n4,5,6", [0, 1]) == "1,2\n4,5")
    print(csv_columns("a,b,c,d,e\n1,2,3,4,5\nf,g,h,i,j", [1, 3, 5, 7]) == "b,d\n2,4\ng,i")
    print(csv_columns("1\n2\n3\n4\n5", [0, 1]) == "1\n2\n3\n4\n5")
    print(csv_columns("1\n2\n3\n4\n5", [1]) == "")
    print(csv_columns("4\n9\n7", [0, 1, 0, 0, 0, 2, 1, 2, 1, 1]), '4\n9\n7')