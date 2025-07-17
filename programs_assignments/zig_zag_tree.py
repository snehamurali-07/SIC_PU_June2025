class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_edge(root, u, v, c):
    if root is None:
        return
    if root.data == u:
        if c == 'L':
            root.left = Node(v)
        else:
            root.right = Node(v)
    else:
        insert_edge(root.left, u, v, c)
        insert_edge(root.right, u, v, c)

def zigzag_traversal(root):
    if not root:
        return

    result = []
    current_level = [root]
    left_to_right = True

    while current_level:
        level_values = []
        next_level = []

        for node in current_level:
            level_values.append(node.data)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if not left_to_right:
            level_values.reverse()
        
        result.extend(level_values)
        current_level = next_level
        left_to_right = not left_to_right

    print(' '.join(map(str, result)))

n = int(input())

edges = []
for _ in range(n - 1):
    u, v, c = input().split()
    edges.append((int(u), int(v), c))

root = Node(edges[0][0])
for u, v, c in edges:
    insert_edge(root, u, v, c)

zigzag_traversal(root)