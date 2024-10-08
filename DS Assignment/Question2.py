#Implement Queues using stack: leetcode id - 1278583536

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2.pop()
        return -1

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2[-1]
        return -1

    def empty(self):
        return not self.s1 and not self.s2
