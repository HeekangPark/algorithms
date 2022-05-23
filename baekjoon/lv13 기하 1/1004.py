import sys
import json
input = sys.stdin.readline

T = int(input())
for t in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    data = []
    for c_idx in range(n):
        cx, cy, r = map(int, input().split())
        data.append((cx, cy, r, c_idx))

    data = sorted(data, key=lambda x: x[2], reverse=True)

    def is_in(c1x, c1y, r1, c2x, c2y, r2):
        return (c1x - c2x) ** 2 + (c1y - c2y) ** 2 <= (r1 + r2) ** 2

    def place(roots, cx, cy, r, c_idx):
        is_placed = False
        for root in roots:
            if is_in(root["cx"], root["cy"], root["r"], cx, cy, r):
                place(root["childs"], cx, cy, r, c_idx)
                is_placed = True
                break
        
        if not is_placed:
            roots.append({"cx": cx, "cy": cy, "r": r, "idx": c_idx, "childs": []})

    def set_parent(roots, path):
        for root in roots:
            parents[root["idx"]] = [x for x in path] + [root["idx"]]
            set_parent(root["childs"], path + [root["idx"]])

    def find_circle(c_idx, roots, x, y):
        target = None
        for root in roots:
            if is_in(root["cx"], root["cy"], root["r"], x, y, 0):
                target = root
        
        if target is None:
            return c_idx
        else:
            return find_circle(target["idx"], target["childs"], x, y)

    roots = []
    for cx, cy, r, c_idx in data:
        place(roots, cx, cy, r, c_idx)
    
    parents = [None] * n
    set_parent(roots, [-1])

    c1 = find_circle(-1, roots, x1, y1)
    c2 = find_circle(-1, roots, x2, y2)

    c1_parents = parents[c1][::-1] if c1 != -1 else [-1]
    c2_parents = parents[c2][::-1] if c2 != -1 else [-1]

    for i in range(len(c2_parents)):
        if c2_parents[i] in c1_parents:
            j = c1_parents.index(c2_parents[i])
            print(i + j)
            break

    