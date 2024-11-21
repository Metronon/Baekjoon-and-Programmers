from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
        
    def push(self, item):
        self.items.append(item)
        
    def empty(self):
        return 1 if len(self.items == 0) else 0
        
    def pop(self):
        if not self.empty():
            return self.items.popleft()
        return -1
    
    def size(self):
        return len(self.items)
    
    def front(self):
        if len(self.items) == 0:
            return -1
        return self.items[0]
    
    def back(self):
        if len(self.items) == 0:
            return -1
        return self.items[-1]
    
queue = Queue()

N = int(input())

commands = { 
    "push": lambda x: queue.push(int(x[1])), 
    "pop": lambda x: print(queue.pop()), 
    "size": lambda x: print(queue.size()), 
    "empty": lambda x: print(queue.empty()), 
    "front": lambda x: print(queue.front()), 
    "back": lambda x: print(queue.back()) 
}

for i in range(N):
    command = input().strip.split()
    if command[0] in commands:
        commands[command[0]](command)
