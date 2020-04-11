# 이진 트리에서 두 노드사이의 거리 구하기
# 조건 01 : 전체 점수의 처음부터 끝까지 반복하여 현재의 점수가 몇 번쨰의 크기를 갖는지를 계산한다.
# 조건 02 : 이진트리에서 두 노드의 거리는 두 노드가 루트 노드가 될 때까지 부모 노드를 구하면 된다.

# 힌트
# 힌트 01 : 주어진 노드 n의 부모 노드는 n/2가 된다.
# 힌트 02 : 두 노드의 거리는 두 노드가 루트 노드가 될 때까지 부모 노드를 구하면 된다.

def f(a, b):
    if a == b:
        return 0

    if b > a:
        return f(a, b // 2) + 1

    if a > b:
        return f(a // 2, b) + 1

if __name__=='__main__':
    a = int(input('첫 번째 노드 : '))
    b = int(input('두 번째 노드 : '))
    print('%d와 %d의 거리 : %d' % (a, b, f(a, b)))