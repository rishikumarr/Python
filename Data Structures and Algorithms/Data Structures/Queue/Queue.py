from collections import deque
queue = deque()
queue.appendleft(5)  # First In
queue.appendleft(10)
queue.appendleft(15)
print(queue.pop())  # output will be 5 # First Out
print(queue)
