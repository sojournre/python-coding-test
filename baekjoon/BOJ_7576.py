import pprint
from collections import deque

M, N = map(int, input().split())
tomatos = []

for _ in range(N):
    tomato = list(map(int, input().split()))
    tomatos.append(tomato)

# 익은 토마토를 queue에 담아준다.
queue = deque()
for i in range(len(tomatos)):
    for j in range(len(tomatos[0])):
        if tomatos[i][j] == 1:
            queue.append([i, j])


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0

    while queue:
        count += 1  # 일수 증가
        for _ in range(len(queue)):
            a, b = queue.popleft()

            # 동서남북 4방향으로 이동
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                # 창고의 범위안에 아직 안 익은 토마토가 있는 경우
                if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0:
                    tomatos[nx][ny] = 1
                    queue.append([nx, ny])

    # queue 다 돌고 나서도 익지 않은 토마토가 남은 경우 -1 리턴
    for i in range(len(tomatos)):
        for j in range(len(tomatos[0])):
            if tomatos[i][j] == 0:
                return -1

    # 모두 익은 경우 일수 출력
    # 마지막에 익은 토마토가 queue 에 들어가서 while 문이 한번 더 돌기 때문에 -1 해줌
    return count - 1


pp = pprint.PrettyPrinter()
pp.pprint(tomatos)
print(bfs())
