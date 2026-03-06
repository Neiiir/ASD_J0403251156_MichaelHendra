class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        antrianBaru = Node(data)
        if self.is_empty():
            self.front = antrianBaru
            self.rear = antrianBaru
            return

