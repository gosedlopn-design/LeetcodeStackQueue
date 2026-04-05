class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x):
        node = Node(x)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def peek(self):
        if self.head is not None:
            return self.head.data
        return None

    def pop(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def is_empty(self):
        return self.head is None

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.push(x)
        while not self.q1.is_empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()
