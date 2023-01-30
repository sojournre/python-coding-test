from sys import stdin

input = stdin.readline

n = int(input())
nums = [0] * 10001
for _ in range(n):
    num = int(input())
    nums[num] += 1

for i in range(len(nums)):
    if i != 0:
        for _ in range(nums[i]):
            print(i)
