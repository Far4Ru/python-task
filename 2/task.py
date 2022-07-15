from collections import deque

class BufferList:
    def __init__(self):
        self.queue = []
    def add(self, x):
        return self.queue.insert(0, x)
    def pop(self):
        return self.queue.pop()
    
    def isEmpty(self):
        return len(self.queue) == 0
    def first(self):
        return self.queue[-1]
    def last(self):
        return self.queue[0]

class BufferDeque:
    def __init__(self):
        self.queue = deque()
    def add(self, x):
        return self.queue.appendleft(x)
    def pop(self):
        return self.queue.pop()
    
    def isEmpty(self):
        return len(self.queue) == 0
    def first(self):
        return self.queue[-1]
    def last(self):
        return self.queue[0]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class BufferNode:
    def __init__(self):
        self.last = None
        self.first = None
    def add(self, x):
        node = Node(x)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
    def pop(self): 
        temp = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return temp.data

    def isEmpty(self):
        return self.last is None and self.first is None
    def first(self):
        return self.first
    def last(self):
        return self.last
