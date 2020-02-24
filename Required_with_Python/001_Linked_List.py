# 연결 리스트
# 시간적인 효율성은 배열보다 좋다.
# 배열에 비해 연결 리스트는 삽입 알고리즘과 마찬가지로 메모리를 할당하고,
# 또 삭제한 메모리를 해제하기 떄문에 공간적인 효율성이 높다.
# 삽입 알고리즘과 마찬가지로 배열의 경우에는 인덱스로 처리하기 때문에 개념적으로 이해하기는 연결 리스트보다 배열이 더 쉽다.

# 노드 정의
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 리스트 초기화
def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")

    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E

# 노드 삭제
def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next

    if pre_node.data == del_data:
        node_A = next_node
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next

# 노드 삽입
def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A

    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next

    new_node.next = node_T
    node_P.next = new_node

# 노드 출력
def print_list():
    global node_A
    node = node_A

    while node:
        print(node.data)
        node = node.next
    print

# 메인
if __name__ == '__main__':
    print("연결 리스트 초기화 후")
    init_list()
    print_list()
    print("노드 C를 추가한 후")
    insert_node("C")
    print_list()