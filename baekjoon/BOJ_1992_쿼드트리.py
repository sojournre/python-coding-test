N = int(input())
board = [list(map(int, input())) for _ in range(N)]


def dnc(x, y, n):
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        dnc(x, y, n)
        dnc(x, y + n, n)
        dnc(x + n, y, n)
        dnc(x + n, y + n, n)
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


dnc(0, 0, N)
