class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#inOrder traversal without recursion
def inOrder(root):
    cur = root
    s = []
    done = 0

    while not done:
        if cur is not None:
            s.append(cur)
            cur = cur.left
        else:
            if(len(s) > 0):
                cur = s.pop()
                print(cur.val)
                cur = cur.right
            else:
                done = 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)