import collections
import heapq


def solution(satisfy, k):
    # answer = 0
    # if len(satisfy) <= 2:
    #     return max(satisfy)
    #
    # dp = collections.OrderedDict()
    # dp[0], dp[1] = satisfy[0], max(satisfy[0], satisfy[1])
    # for i in range(2, len(satisfy)):
    #     dp[i] = max(dp[i - 1], dp[i - 2] + satisfy[i])
    # print(dp)
    # return dp.popitem()[1]

    n = len(satisfy)
    l = list(range(-1, n-1))    # 왼쪽 index
    r = list(range(1, n+1))     # 오른쪽 index
    l[0] = n - 1
    r[n - 1] = 0
    visit = [0 for _ in range(n)]   # 식사를 할 수 있는지

    hq = [(-s, i) for i, s in enumerate(satisfy)]
    heapq.heapify(hq)

    ans = 0
    while hq and k:
        s, idx = heapq.heappop(hq)
        if visit[idx]:
            continue
        ans += -s
        satisfy[idx] = satisfy[l[idx]] + satisfy[r[idx]] - satisfy[idx]
        if satisfy[idx] > 0:
            heapq.heappush(hq, (-satisfy[idx], idx))
        visit[l[idx]] = visit[r[idx]] = True
        l[idx] = l[l[idx]]
        r[idx] = r[r[idx]]
        l[r[idx]] = idx
        r[l[idx]] = idx
        k -= 1

    return ans


satisfy = [5, 4, 4, 6, 2, 1, 3]
k = 3
# result = 13
sol = solution(satisfy, k)
print(sol)

