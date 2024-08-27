class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get_first(self):
        if self.first is not None:
            print(f"First: {self.first.value}")
        else:
            print("Queue is empty.")

    def get_last(self):
        if self.last is not None:
            print(f"Last: {self.last.value}")
        else:
            print("Queue is empty.")

    def get_length(self):
        print(f"Length: {self.length}")


# Example usage:
queue = Queue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.print_queue()
queue.get_first()
queue.get_last()
queue.get_length()
dequeued_node = queue.dequeue()
print(f"Dequeued: {dequeued_node.value if dequeued_node else 'None'}")
queue.print_queue()
queue.get_first()
queue.get_last()
queue.get_length()
