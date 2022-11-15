n, m = map(int, input().split())
card = list(map(int, input().split()))
three = 0
ans = 0
card.sort()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            three = card[i] + card[j] + card[k]
            if three > m:
                break
            ans = max(three, ans)
print(ans)

