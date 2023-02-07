n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
# print(arr)
for i in arr:
    count = 1
    for j in arr:
        if j[0] > i[0] and j[1] > i[1]:
            count += 1
    print(count, end=" ")
