import sys

nums = ["666"]
digit_till = {
    3: 1,
}

n = int(input())

def check(nums, n):
    if len(nums) >= n:
        print(nums[n - 1])
        sys.exit(0)

def build(nums, n, digit, depth):
    if (digit == 4 and depth == 2) or (digit == 5 and depth == 3) or depth == 4:
        nums += [f"666{str(back).zfill(digit - 3)}" for back in range(int(10 ** (digit - 3)))]
        check(nums, n)
        return

    new_nums = []
    for front in range((1 if depth == 1 else 0), 6):
        for item in nums[:digit_till[digit - depth]]:
            new_nums.append(f"{'6' * (depth - 1)}{front}{item.zfill(digit - depth)}")
    nums += new_nums
    check(nums, n)

    build(nums, n, digit, depth + 1)

    new_nums = []
    for front in range(7, 10):
        for item in nums[:digit_till[digit - depth]]:
            new_nums.append(f"{'6' * (depth - 1)}{front}{item.zfill(digit - depth)}")
    nums += new_nums
    check(nums, n)

digit = 3
check(nums, n)

digit = 4
build(nums, n, digit, 1)
digit_till[digit] = len(nums)

digit = 5
build(nums, n, digit, 1)
digit_till[digit] = len(nums)

while True:
    digit += 1
    build(nums, n, digit, 1)
    digit_till[digit] = len(nums)