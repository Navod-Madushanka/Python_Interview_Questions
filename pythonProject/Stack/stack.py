class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp

    def push(self, value):
        node = Node(value)

        if self.top is not None:
            node.next = self.top

        self.top = node
        self.height += 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get_top(self):
        if self.top is not None:
            print(f"Top: {self.top.value}")
        else:
            print("Stack is empty.")

    def get_height(self):
        print(f"Height: {self.height}")


if __name__ == "__main__":
    stack = Stack(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    stack.print_stack()
