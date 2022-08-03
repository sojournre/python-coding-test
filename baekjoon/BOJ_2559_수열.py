import collections
from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
degree = list(map(int, input().split()))

result = [sum(degree[:K])]

for i in range(N - K):
    # result.append(sum(degree[i:i + K])) 시간초과 발생
    result.append(result[i] - degree[i] + degree[K + i])

print(max(result))

