n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
# 나의 풀이
# ans = price[0] * distance[0]
# min_price = price[0]
#
# for i in range(1, len(distance)):
#     min_price = min(min_price, price[i])
#     ans += min_price * distance[i]

# 참고 풀이
ans = 0
min_price = price[0]
for i in range(n - 1):
    if price[i] < min_price:
        min_price = price[i]
    ans += min_price * distance[i]
print(ans)
