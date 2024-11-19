![image](https://github.com/user-attachments/assets/55c0cbfd-1984-41ae-9deb-482fe98693ff)

파이썬에서는 Stack 또는 Queue에 대한 명령어가 구현되어있지 않기 때문에 class를 이용해 직접 구현해야한다.

입력조건은 N은 1 <= N <= 2,000,000 이고, 주어지는 정수는 1 <= X <= 100,000 이다.
정수의 크기는 상관없고 N이 최대 2,000,000까지 주어졌기 때문에 명령어를 미리 입력한후 반복문을 실행하게 작성했다.

```py
from collections import deque

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
    
n_queue = Queue()

N = int(input())

commands = { 
    "push": lambda x: n_queue.push(int(x[1])), 
    "pop": lambda x: print(n_queue.pop()), 
    "size": lambda x: print(n_queue.size()), 
    "empty": lambda x: print(n_queue.empty()), 
    "front": lambda x: print(n_queue.front()), 
    "back": lambda x: print(n_queue.back()) 
}

for i in range(N):
    command = input().strip().split()
    if command[0] in commands:
        commands[command[0]](command)
```

18258번 문제의 경우 pypy3, python3 의 시간제한을 3초로 주어줬지만, 두 방식 모두 시간초과가 났다.
다른 방식을 찾아서 코드를 수정해야할 것 같다.
