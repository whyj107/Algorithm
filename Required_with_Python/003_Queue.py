# put : 매표소 앞에서 줄을 선다.
#       데이터를 저장하는 함수
# get : 줄을 선 순서대로 앞에서부터 표를 산다.
#       데이터를 꺼내오는 함수
# FIFO(First In First Out)
# 큐는 배열을 사용하는 것이 좀 더 편리하다.

def put(item):
    queue.append(item)

def get():
    return queue.pop()

if __name__=='__main__':
    queue = []
    put(1)
    put(2)
    put(3)
    put(4)

    print("현재 queue의 모습")
    print(queue)

    while queue:
        print("POP > {}".format(get()))