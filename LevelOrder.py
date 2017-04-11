from Node import Node

def levelOrder(root):
    if root is None:
        return

    q = [root] 
    while len(q) > 0:
       print q[0].val 
       cur = q.pop(0)
       
       if cur.left is not None:
           q.append(cur.left)
       if cur.right is not None:
           q.append(cur.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

levelOrder(root)