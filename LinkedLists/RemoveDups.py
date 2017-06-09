from Node import Node

def remove_dups(node):
    if node is None:
        return
    
    vals = set()
    vals.add(node.val)

    prev = node
    cur = node.next

    while cur is not None:
        if cur.val in vals:
            prev.next = cur.next
            cur = cur.next
        else:
            vals.add(cur.val)
            prev = prev.next
            cur = cur.next

            
node = Node(1)
node.next = Node(2)
node.next.next = Node(1)

node2 = Node(1)
node2.next = Node(1)
node2.next.next = Node(2)
node2.next.next.next = Node(1)
node2.next.next.next.next = Node(1)

remove_dups(node2)


while node2 is not None:
    print(node2.val)
    node2 = node2.next
