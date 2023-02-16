def solution(grid):
    visit = [[False for i in range(len(grid))] for j in range(len(grid[0]))]

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visit[i][j] != '#':
            return False

        # grid[i][j] = '.'
        visit[i][j] = True
        # 상하좌우 대각 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i - 1, j - 1)
        dfs(i - 1, j + 1)
        dfs(i + 1, j - 1)
        dfs(i + 1, j + 1)
        return True

    answer = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                if dfs(i, j):
                    answer += 1
    return answer


grid = [".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]
print(solution(grid))
