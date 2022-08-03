import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = list()
        for i in matrix:
            for j in i:
                heapq.heappush(heap, j)

        for _ in range(1, k):
            heapq.heappop(heap)

        return heapq.heappop(heap)


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

kth_smallest = Solution().kthSmallest(matrix, k)
print(kth_smallest)
