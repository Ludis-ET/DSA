class Node:
    def __init__(self,value = None) -> None:
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

s = SLinkedList()
node1 = Node(1)
node2 = Node(2)


s.head = node1
s.head.next = node2
s.tail = node2