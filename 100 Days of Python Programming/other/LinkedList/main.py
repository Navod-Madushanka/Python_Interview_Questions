class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class sll:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


linkedList = sll()
node_1 = node(4)
node_2 = node(9)

linkedList.head = node_1
node_1.next = node_2
linkedList.tail = node_2

for node in linkedList:
    print(node.value, end= ", ")