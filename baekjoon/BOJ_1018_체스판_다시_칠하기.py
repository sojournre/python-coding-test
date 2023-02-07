n, m = map(int, input().split())
# board = []
# for _ in range(n):
#     board.append(input())

board = [input() for _ in range(n)]
# print(board)
cnt = []
i = 0
while i < n - 7:
    j = 0
    while j < m - 7:
# for i in range(n - 7):
#     for j in range(m - 7):
        draw_w = 0
        draw_b = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        draw_w += 1
                    else:
                        draw_b += 1
                else:
                    if board[a][b] != 'W':
                        draw_b += 1
                    else:
                        draw_w += 1

        cnt.append(draw_w)
        cnt.append(draw_b)

        j += 1
    i += 1
# print(cnt)
print(min(cnt))
