class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            return self.items.pop()
    
    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self.items[-1]
    
    def push(self, X):
        self.items.append(X)

    def parseCmd(self, cmdline):
        if cmdline.startswith("push"):
            self.push(int(cmdline[5:]))
        elif cmdline.startswith("pop"):
            print(self.pop())
        elif cmdline.startswith("size"):
            print(self.size())
        elif cmdline.startswith("empty"):
            print(self.empty())
        elif cmdline.startswith("top"):
            print(self.top())

import sys
s = Stack()
n = int(sys.stdin.readline())
for _ in range(n):
    s.parseCmd(sys.stdin.readline())