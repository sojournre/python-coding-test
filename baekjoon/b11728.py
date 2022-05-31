_ = map(int, input().split())
ab = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = a + b
ab.sort()
# print(ab)
print(*ab)
