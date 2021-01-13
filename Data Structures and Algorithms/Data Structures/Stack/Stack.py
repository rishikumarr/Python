from collections import deque
stack = deque()
# print(dir(stack))
# 'append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 
# 'index', 'insert', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate'
stack.append(1)
print(stack.pop())
print(stack)
# Stack follows Last In First Out, so we're only using append and pop.
# Insertion and Deletion should be happen in only one end in stack