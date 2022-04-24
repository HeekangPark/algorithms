x, y, w, h = map(int, input().split())

# up, down, left, right
distance = [h - y, y, x, w - x]
print(min(distance))
