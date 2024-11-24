from collections import deque
import sys

class Deque:
    def __init__(self):
        self.temp_deque = deque()
        
    def addLeft(self, num):
        self.temp_deque.appendleft(num)
        
    def addRight(self, num):
        self.temp_deque.append(num)
        
    def popLeft(self):
        if len(self.temp_deque) == 0:
            return -1
        return self.temp_deque.popleft()
    
    def popRight(self):
        if len(self.temp_deque) == 0:
            return -1
        return self.temp_deque.pop()
    
    def length(self):
        return len(self.temp_deque)
    
    def isEmpty(self):
        if len(self.temp_deque) == 0:
            return 1
        return 0
    
    def printLeft(self):
        if len(self.temp_deque) == 0:
            return -1
        return self.temp_deque[0]
    
    def printRight(self):
        if len(self.temp_deque) == 0:
            return -1
        return self.temp_deque[-1]

cmd = Deque()

commands = {
    1: lambda x: cmd.addLeft(x),
    2: lambda x: cmd.addRight(x),
    3: lambda _: print(cmd.popLeft()),
    4: lambda _: print(cmd.popRight()),
    5: lambda _: print(cmd.length()),
    6: lambda _: print(cmd.isEmpty()),
    7: lambda _: print(cmd.printLeft()),
    8: lambda _: print(cmd.printRight())
}

input = sys.stdin.read
data = input().splitlines()

A = int(data[0])
for i in range(1, A + 1):
    command = data[i].split()
    N = int(command[0])
    
    if N in (1, 2):
        M = int(command[1])
        commands[N](M)
    else:
        commands[N](None)

