class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur = self.head
        while cur.next!= None:
            cur = cur.next
        new_node = Node(data)
        cur.next = new_node

    def __str__(self):
        elem = []
        cur = self.head
        while cur.next!= None:
            cur = cur.next
            elem.append(cur.data)
        return str(elem)

# n1 = Node(1)
# n2 = Node(2)
# n1.next = n2
#
#
# print(n1)
# print(n2)
lst = SingleLinkedList()
print(lst)
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)
