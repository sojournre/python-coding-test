w, h, b = map(int, input().split())

ans = w * h * b / 8 / 1024 / 1024
print('%.2f' % ans, "MB")
print(f"{3.55555:.4f}")
