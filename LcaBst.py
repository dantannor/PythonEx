from Node import Node
#Lowest common ancestor in a BST
def lca(root, n1, n2):
    if root is None:
        return None
    if(root.val > n1 and root.val < n2):
        return root
    if root.val > n1 and root.val > n2:
        lca(root.left, n1, n2) 
    elif root.val < n1 and root.val < n2:
        lca(root.right, n1, n2)
    
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
 
 
n1 = 10 ; n2 = 22
t = lca(root, n1, n2)
print "LCA of %d and %d is %d" %(n1, n2, t.val)
