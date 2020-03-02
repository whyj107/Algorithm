# 트리에서 사용할 노드(Node) 클래스의 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 전위 순휘 알고리즘(Preorder Traverse)
# 가운데 노드를 먼저 방문하고 그 다음에는 왼쪽 노드를 방문하고
# 그리고 나서 오른쪽 노드를 방문하는 방법
def preorder_traverse(node):
    if node == None: return
    print(node.data, end=' -> ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)

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
    print("< Preorder Traverse >")
    preorder_traverse(root)