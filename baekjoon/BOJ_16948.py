# 1. dfs 로 아래만큼 이동하면서 (r2, c2) 가 될 때까지 재귀호출
# 2. 더 이상 이동할 수 없을 때까지 방문했는데도 (r2, c2)가 안되면 -1 출력
N = int(input())
r1, c1, r2, c2 = map(int, input().split())




dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
