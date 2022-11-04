n = int(input())
s = 0
i = 1
while s < n:
    s += i
    if s >= n:
        print(i)
    else:
        i += 1
