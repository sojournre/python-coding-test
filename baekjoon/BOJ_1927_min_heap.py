import heapq
from sys import stdin

input = stdin.readline

N = int(input())
heap = list()
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
