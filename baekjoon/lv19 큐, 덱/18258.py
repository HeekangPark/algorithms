from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def size(self):
        return len(self.items)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def push(self, X):
        self.items.append(X)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.items.popleft()

    def front(self):
        if self.empty():
            return -1
        else:
            return self.items[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.items[-1]

    def parse(self, cmdline):
        if cmdline.startswith('push'):
            self.push(int(cmdline.split()[1]))
        elif cmdline.startswith('pop'):
            print(self.pop())
        elif cmdline.startswith('size'):
            print(self.size())
        elif cmdline.startswith('empty'):
            print(self.empty())
        elif cmdline.startswith('front'):
            print(self.front())
        elif cmdline.startswith('back'):
            print(self.back())

import sys

queue = Queue()
n = int(sys.stdin.readline())
for _ in range(n):
    cmdline = sys.stdin.readline().strip()
    queue.parse(cmdline)


