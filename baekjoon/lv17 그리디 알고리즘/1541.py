line = input().strip()

buffer = 0
num = 0
is_buffer_on = False
result = 0
for c in line:
    if c == "+":
        if is_buffer_on:
            buffer += num
        else:
            result += num
        num = 0
    elif c == "-":
        if is_buffer_on:
            buffer += num
            result -= buffer
            buffer = 0
        else:
            result += num
            is_buffer_on = True
            buffer = 0
        num = 0
    else:
        num = num * 10 + int(c)

if is_buffer_on:
    buffer += num
    result -= buffer
else:
    result += num

print(result)
