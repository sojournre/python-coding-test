import heapq
from sys import stdin

input = stdin.readline

N = int(input())
heap = list()
for _ in range(N):
    a = list(map(int, input().split()))
    if a[0] != 0:
        for i in a[1:]:
            heapq.heappush(heap, -i)
    else:
        try:
            print(-heapq.heappop(heap))
        except:
            print(-1)
