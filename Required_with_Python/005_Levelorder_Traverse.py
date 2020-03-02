# 트리에서 사용할 노드(Node) 클래스의 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

levelq = []
# 단계 순위 순회 알고리즘(Levelorder Traverse)
# 단계 순서대로 왼쪽부터 오른쪽으로 방문하는 순회 알고리즘
def levelorder_traverse(node):
    global levelq
    levelq.append(node)
    while len(levelq) != 0:
        # visit
        visit_node = levelq.pop(0)
        print(visit_node.data, end=' -> ')

        # child put
        if visit_node.left != None:
            levelq.append(visit_node.left)
        if visit_node.right != None:
            levelq.append(visit_node.right)

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
    print("< Levelorder Traverse >")
    levelorder_traverse(root)