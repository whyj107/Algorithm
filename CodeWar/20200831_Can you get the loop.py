# 문제
# Can you get the loop?
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

# 풀이
def loop_size(node):
    a, b = node.next, node.next.next
    while a != b:
        a = a.next
        b = b.next.next
    cnt = 1
    b = b.next
    while a != b:
        cnt += 1
        b = b.next
    return cnt

def loop_size1(node):
    index = {}
    i = 0
    while True:
        if node in index:
            return i - index[node]
        index[node] = i
        node = node.next
        i += 1

class Node():
    def __init__(self):
        self.next = Node

if __name__ == '__main__':
    # Make a short chain with a loop of 3
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(loop_size(node1), 3, 'Loop size of 3 expected')

    """
    # Make a longer chain with a loop of 29
    nodes = [Node() for _ in xrange(50)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[49].next = nodes[21]
    print(loop_size(nodes[0]), 29, 'Loop size of 29 expected')

    # Make a very long chain with a loop of 1087
    chain = create_chain(3904, 1087)
    print(loop_size(chain), 1087, 'Loop size of 1087 expected')
    """