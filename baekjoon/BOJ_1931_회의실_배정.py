import heapq
from sys import stdin

input = stdin.readline

N = int(input())
heap = []
for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(heap, (end, start))

first = heapq.heappop(heap)
pre_end = first[0]
result = 1
while heap:
    time = heapq.heappop(heap)
    if time[1] >= pre_end:
        result += 1
        pre_end = time[0]

print(result)
