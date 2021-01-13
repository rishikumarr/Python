from collections import deque
# 'append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 
# 'index', 'insert', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate'
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,item):
        return self.container.append(item)
    def pop(self):
        return self.container.pop()
    def size(self):
        print(len(self.container))
    def is_empty(self):
        if len(self.container) == 0:
            print(True)
        else:
            print(False)
    def peek(self):
        print(self.container[-1])
        
s = Stack()
s.push(3)
s.pop()
s.size()
s.is_empty()
s.push(4)
s.peek()
print(s.container)