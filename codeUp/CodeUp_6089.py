a, r, n = map(int, input().split())
s = a
for i in range(2, n + 1):
    s *= r
print(s)
