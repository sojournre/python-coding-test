def solution(n, horizontal):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    # R, D, L, U
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    if horizontal:
        direction = 0
    else:
        direction = 1

    for cnt in range(1, n * n + 1):
        answer[x][y] = cnt
        x += dx[direction]
        y += dy[direction]

        if x > cnt or y > cnt:


        # if x < 0 or y < 0 or x >= n or y >= n or answer[x][y]:
        #     x -= dx[direction]
        #     y -= dy[direction]
        #
        #     direction = (direction + 1) % 4
        #     x += dx[direction]
        #     y += dy[direction]

    for i in answer:
        print(*i, ' ')

    return answer


n = 4
horizontal = True
# print(solution(n, horizontal))
solution(n, horizontal)

n = 5
horizontal = False
# print(solution(n, horizontal))
solution(n, horizontal)
