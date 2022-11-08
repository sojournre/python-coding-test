n = int(input())
a = list(map(int, input().split()))
# min_number = min(a)
# print(min_number)
min_number = a[0]

for i in range(1, n):
    if a[i] < min_number:
        min_number = a[i]

print(min_number)
