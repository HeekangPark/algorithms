from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def size(self):
        return len(self.items)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def push_front(self, X):
        self.items.appendleft(X)

    def push_back(self, X):
        self.items.append(X)

    def pop_front(self):
        if self.empty():
            return -1
        else:
            return self.items.popleft()
    
    def pop_back(self):
        if self.empty():
            return -1
        else:
            return self.items.pop()

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
        if cmdline.startswith('push_front'):
            self.push_front(int(cmdline.split()[1]))

        elif cmdline.startswith('push_back'):
            self.push_back(int(cmdline.split()[1]))

        elif cmdline.startswith('pop_front'):
            print(self.pop_front())

        elif cmdline.startswith('pop_back'):
            print(self.pop_back())

        elif cmdline.startswith('size'):
            print(self.size())

        elif cmdline.startswith('empty'):
            print(self.empty())

        elif cmdline.startswith('front'):
            print(self.front())

        elif cmdline.startswith('back'):
            print(self.back())

import sys
n = int(sys.stdin.readline())
dq = Deque()
for _ in range(n):
    cmdline = sys.stdin.readline().strip()
    dq.parse(cmdline)