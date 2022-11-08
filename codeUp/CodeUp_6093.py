n = int(input())
# a = list(map(int, input().split()))
a = input().split()
# print(a)

for i in range(n-1, -1, -1):
    print(a[i], end=' ')
