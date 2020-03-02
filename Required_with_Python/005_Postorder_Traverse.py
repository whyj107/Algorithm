# 트리에서 사용할 노드(Node) 클래스의 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 후위 순회 알고리즘(Postorder Traverse)
# 왼쪽 자식 노드를 방문하고 다음에 오른쪽 자식 노드를 방문한 후에 마지막으로 부모 노드를 방문하는 알고리즘
def postorder_traverse(node):
    if node == None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end=' -> ')

root = None

# 트리의 초기화
def init_tree():
    global root
    new_node = Node("A")
    root = new_node

    new_node = Node("B")
    root.left = new_node

    new_node = Node("C")
    root.right = new_node

    new_node_1 = Node("D")
    new_node_2 = Node("E")

    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    new_node_1 = Node("F")
    new_node_2 = Node("G")

    node = root.right
    node.left = new_node_1
    node.right = new_node_2

# 순회 프로그램의 시작점
if __name__=='__main__':
    init_tree()
    print("< Postorder Traverse >")
    postorder_traverse(root)