import heapq


def solution(scoville, K):
    s1 = 0
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)
    while True:
        s1 = heapq.heappop(scoville)
        if s1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        s2 = heapq.heappop(scoville)
        s = s1 + 2 * s2
        heapq.heappush(scoville, s)
        # print(scoville)
        answer += 1
    return answer


scoville = [1, 1, 1]
k = 100
sol = solution(scoville, k)
print(sol)
