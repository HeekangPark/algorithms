t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    input_line = input()
    if len(input_line[1:-1]) > 0:
        a = [0] + list(map(int, input_line[1:-1].split(",")))
    else:
        a = [0]

    is_printed = False
    is_reversed = False
    length = n
    head = 1
    tail = n
    for c in p:
        if c == "R":
            head, tail = tail, head
            is_reversed = not is_reversed
        else: # c == "D"
            if length == 0:
                print("error")
                is_printed = True
                break
            else:
                if is_reversed:
                    head -= 1
                else:
                    head += 1
                length -= 1
    
    if not is_printed:
        if is_reversed:
            print(f"[{','.join(map(str, a[head:tail - 1:-1]))}]")
        else:
            print(f"[{','.join(map(str, a[head:tail + 1:1]))}]")
            
