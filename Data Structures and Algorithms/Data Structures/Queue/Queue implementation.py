from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self,item):
        self.queue.appendleft(item)
    def dequeue(self):
        return self.queue.pop()
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
# print(q.is_empty()) # False
# print(q.queue)       # deque([15,10,5]) 
# print(q.dequeue()) # 5
# print(q.dequeue()) # 10
# print(q.dequeue()) # 15
# print(q.is_empty()) # True
# print(q.queue)       # deque([])