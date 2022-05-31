# 참고 사이트
# https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2346-%ED%92%8D%EC%84%A0-%ED%84%B0%EB%9C%A8%EB%A6%AC%EA%B8%B0-deque

from collections import deque

N = int(input())
a = list(map(int, input().split()))

b = list(enumerate(a, start=1))

deq = deque(b)
ans = list()

while deq:
    i, v = deq.popleft()
    if v > 0:
        # 이미 현재 풍선을 pop 했기 때문에 반시계방향으로 1칸씩 회전된 상태이므로 -1을 해준다.
        deq.rotate(-(v - 1))
    else:
        # 마찬가지로 현재 풍선이 pop 된 상태이지만 시계방향으로 회전하므로 -1 해줄 필요가 없다.
        deq.rotate(-v)
    ans.append(i)
print(*ans)
