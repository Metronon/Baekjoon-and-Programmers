from collections import deque
import sys
input = sys.stdin.readline
output = sys.stdout.write

class Queue:
    def __init__(self):
        self.items = deque()
        
    def push(self, item):
        self.items.append(item)
        
    def empty(self):
        return 1 if len(self.items) == 0 else 0
        
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

N = int(input().strip())

commands = { 
    "push": lambda x: queue.push(int(x[1])), 
    "pop": lambda _: output(f"{queue.pop()}\n"), 
    "size": lambda _: output(f"{queue.size()}\n"), 
    "empty": lambda _: output(f"{queue.empty()}\n"), 
    "front": lambda _: output(f"{queue.front()}\n"), 
    "back": lambda _: output(f"{queue.back()}\n") 
}

for _ in range(N):
    command = input().strip().split()
    if command[0] in commands:
        commands[command[0]](command)