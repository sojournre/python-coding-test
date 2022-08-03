import bisect
import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    cd_n = [int(input()) for _ in range(N)]
    cd_m = [int(input()) for _ in range(M)]
    result = set()
    for n1 in cd_n:
        # 이진 검색으로 일치 여부 판별
        i2 = bisect.bisect_left(cd_m, n1)
        if n1 == cd_m[i2]:
            result.add(n1)

    print(len(result))
