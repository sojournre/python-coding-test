nums = []
for _ in range(5):
    nums.append(int(input()))

print(round(sum(nums) / len(nums)))
nums.sort()
print(nums[2])
