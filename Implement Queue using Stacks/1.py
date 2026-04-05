class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node
    def pop(self):
        if self.top is not None:
            value = self.top.data
            self.top = self.top.next
            return value
        return None
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
class MyQueue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def pop(self) -> int:
        self.peek()
        return self.stack_out.pop()

    def peek(self) -> int:
        if self.stack_out.top is None:
            while self.stack_in.top is not None:
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.top is None and self.stack_out.top is None
