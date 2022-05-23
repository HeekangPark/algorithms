import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
coords = [list(map(int, input().split())) for _ in range(p)]

def is_in(px, py):
    if x <= px <= x + w and y <= py <= y + h:
        return True
    
    cx = x
    cy = y + (h // 2)
    r = h // 2

    if (px - cx) ** 2 + (py - cy) ** 2 <= (r) ** 2:
        return True
    
    cx = x + w
    cy = y + (h // 2)
    r = h // 2

    if (px - cx) ** 2 + (py - cy) ** 2 <= (r) ** 2:
        return True
    
    return False

print(sum(is_in(c[0], c[1]) for c in coords))