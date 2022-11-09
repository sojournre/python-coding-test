h, w = map(int, input().split())
pan = [[0] * w for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    for _ in range(l):
        pan[x - 1][y - 1] = 1
        if d == 0:
            y += 1
        else:
            x += 1

for i in range(h):
    for j in range(w):
        print(pan[i][j], end=' ')
    print()
