# 2 3 2
# 1 10
# 10 10
# 1 2
# 1 2 2

n, m, c = map(int, input().split())
w = []
for i in range(c):
    w.append(list(map(int, input().split())))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(w, a, b)

sum = 0

for i in a:
    for j in b:
        sum += w[i - 1][j - 1]

print(sum)
