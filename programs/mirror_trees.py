def build_tree(n, edges):
    tree = {}
    for i in range(n):
        tree[i + 1] = {'L': None, 'R': None}
    for u, v, d in edges:
        tree[u][d] = v
    return tree

def is_mirror(tree1, tree2, n):
    for i in range(1, n + 1):
        if tree1[i]['L'] != tree2[i]['R']:
            return False
        if tree1[i]['R'] != tree2[i]['L']:
            return False
    return True

# Input
n = int(input())

edges1 = []
for _ in range(n - 1):
    u, v, d = input().split()
    edges1.append((int(u), int(v), d))

edges2 = []
for _ in range(n - 1):
    u, v, d = input().split()
    edges2.append((int(u), int(v), d))

# Build both trees
tree1 = build_tree(n, edges1)
tree2 = build_tree(n, edges2)

# Check and print result
if is_mirror(tree1, tree2, n):
    print("yes")
else:
    print("no")