class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = Node.insert(root.left, data)
        else:
            root.right = Node.insert(root.right, data)
        return root

    def height(root):
        if root is None:
            return -1
        return 1 + max(Node.height(root.left), Node.height(root.right))

num = int(input("Enter a number: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))

tree_root = None
for val in arr:
    tree_root = Node.insert(tree_root, val)

print("Height of the tree:", Node.height(tree_root))
