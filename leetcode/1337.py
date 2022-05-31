from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    ans = {}
    for i in range(len(mat)):
        ans[i] = sum(mat[i])
    ans = sorted(ans, key=ans.get)
    return ans[:k]


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3

print(mat)
print(kWeakestRows(mat, k))
