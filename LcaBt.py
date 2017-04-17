from Node import Node

# Lowest common ancestor in a binary tree
# Find the path to each key and then compare and break at the first different key
def lca(root, n1, n2):
    p1 = path(root, n1)
    p2 = path(root, n2)

    i = 0
    while p1[i] == p2[i]:
        cur = p1[i]
        i+=1
    
    return cur


def path(root, k):
    if root is None:
        return None
    
    if root.val == k:
        return [root.val]
    if root.left is None and root.right is None:
        return None
    
    left = path(root.left, k)
    right = path(root.right, k)
    if left is not None:
        left.insert(0, root.val)
        return left
    if right is not None:
        right.insert(0, root.val)
        return right

node = Node(3)
node.left = Node(1)
node.left.right = Node(2)
node.left.left = Node(0)
node.right = Node(4)
node.right.right = Node(5)

print(lca(node, 0, 4))
