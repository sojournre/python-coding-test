e, s, m = map(int, input().split())
i = 1
j = 1
k = 1
ans = 1
while True:
    if i == e and j == s and k == m:
        break
    if i == 15:
        i = 0
    if j == 28:
        j = 0
    if k == 19:
        k = 0
    ans += 1
    i += 1
    j += 1
    k += 1

print(ans)
