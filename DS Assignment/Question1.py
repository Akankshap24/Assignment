#Implement Stack using Queues: leetcode id - 1278508807

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        self.q2.append(x)
        while(self.q1):
            self.q2.append(self.q1.popleft())
        self.q1, self.q2  = self.q2, self.q1   

    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()
        return None    

           
    def top(self) -> int:
        if (self.q1):
            return self.q1[0]
        return None    

    def empty(self) -> bool:
        return not self.q1


    

        