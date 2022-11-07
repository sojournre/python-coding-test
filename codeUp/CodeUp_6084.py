h, b, c, s = map(int, input().split())

ans = h * b * c * s / 8 / 1024 / 1024

print(round(ans, 1), "MB")
