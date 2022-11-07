# 10
# 1 3 2 2 5 6 7 4 5 9
from collections import Counter

n = int(input())
# a = input().split()
# for i in range(n):
#     a[i] = int(a[i])
#
# d = []
# for i in range(24):
#     d.append(0)
#
# for i in range(n):
#     d[a[i]] += 1
#
# for i in range(1, 24):
#     print(d[i], end=' ')

a = map(int, input().split())
print(a)
cnt = Counter(a)
print(cnt)

for i in range(1, 24):
    print(cnt[i], end=' ')
