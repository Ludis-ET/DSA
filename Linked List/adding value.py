class Node:
    def __init__(self,value = None) -> None:
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insert(self, value , location):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            if location == 0:
                new.next = self.head
                self.head = new
            elif location == -1:
                new.next = None
                self.tail.next = new
                self.tail = new
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                next = temp.next
                temp.next = new
                new.next = next


link = SLinkedList()
link.insert(1,0)
link.insert(1,0)
link.insert(1,0)
link.insert(1,0)
link.insert(1,0)
link.insert(1,0)
link.insert(2,-1)
print([node.value for node in link])