n = int(input())
# 나의 풀이
# for i in range(n):
#     ans = i
#     sum_ = 0
#     while ans > 0:
#         sum_ += ans % 10
#         ans = ans // 10
#     if sum_ + i == n:
#         print(i)
#         break
#     if i == n - 1:
#         print(0)

# 다른 사람 풀이
result = 0
for i in range(1, n):
    lst = list(map(int, str(i)))
    if sum(lst) + i == n:
        result = i
        break

print(result)
