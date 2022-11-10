maze = []

for _ in range(10):
    a = list(map(int, input().split()))
    maze.append(a)
x = y = 1
# 내 풀이
# while True:
#     maze[x][y] = 9
#     if maze[x][y + 1] == 0:
#         y += 1
#     elif maze[x + 1][y] == 0:
#         x += 1
#     elif x == 9 and y == 9:
#         break
#     elif maze[x][y + 1] == 1 and maze[x + 1][y] == 1:
#         break
#     elif maze[x][y + 1] == 2:
#         y += 1
#         maze[x][y] = 9
#         break
#     elif maze[x + 1][y] == 2:
#         x += 1
#         maze[x][y] = 9
#         break

# 모범 답안
while True:
    if maze[x][y] == 0:
        maze[x][y] = 9
    elif maze[x][y] == 2:
        maze[x][y] = 9
        break

    if (maze[x][y + 1] == 1 and maze[x + 1][y] == 1) or (x == 9 and y == 9):
        break

    if maze[x][y + 1] != 1:
        y += 1
    elif maze[x + 1][y] != 1:
        x += 1

for i in range(10):
    for j in range(10):
        print(maze[i][j], end=' ')
    print()
