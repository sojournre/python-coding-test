import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2

    log = 0
    # answer = 0
    for tree in trees:
        if tree >= mid:
            log += tree - mid

    if log >= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
