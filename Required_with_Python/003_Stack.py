# 입력과 출력을 한 방향으로 제한한 알고리즘
# 바닥부터 데이터를 차곡차곡 쌓는 개념
# 푸쉬(Push) : 그릇을 닦아서 찬장에 쌓아 놓는다.
# 팝 (Pop) : 그릇을 사용하기 위해 찬장에서 가장 위에 있는 그릇을 꺼내 온다.
# LIFO(Last In First Out)

def push(item):
    stack.append(item)

def pop():
    return stack.pop()

if __name__=='__main__':
    stack = []
    push(1)
    push(2)
    push(3)
    push(4)

    print("현재 stack의 모습")
    print(stack)

    while stack:
        print("POP > {}".format(pop()))

