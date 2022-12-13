from collections import deque


def solution(rows, columns, max_virus, queries):
    # 나의 풀이
    #     answer = [[]]
    #     rc = [[0] * columns for _ in range(rows)]
    #     print(rc)
    #
    #     for r, c in queries:
    #         if rc[r][c] < 2:
    #             rc[r][c] += 1
    #         else:
    #
    #     return answer
    #
    # def bfs():
    #     dx = [1, 0, -1, 0]
    #     dy = [0, -1, 0, 1]
    #     queue = deque()
    #     while queue:

    grid = [[0] * columns for _ in range(rows)]

    def action(i, j):
        stack = [(i, j)]
        visited = {(i, j)}
        while stack:
            i, j = stack.pop()
            if grid[i][j] < max_virus:
                grid[i][j] += 1
            else:
                for _i, _j in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= _i < rows and 0 <= _j < columns and (_i, _j) not in visited:
                        visited.add((_i, _j))
                        stack.append((_i, _j))

    for i, j in queries:
        action(i - 1, j - 1)

    return grid


rows = 3
columns = 4
max_virus = 2
queries = [[3, 2], [3, 2], [2, 2], [3, 2], [1, 4], [3, 2], [2, 3], [3, 1]]
# return = [[0, 2, 1, 1], [2, 2, 2, 1], [2, 2, 2, 1]]
sol = solution(rows, columns, max_virus, queries)
print(sol)
