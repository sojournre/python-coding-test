def solution(n, lost, reserve):
    answer = 0
    # lost.sort()
    # reserve.sort()
    # new_lost = [l for l in lost if l not in reserve]
    # new_reserve = [r for r in reserve if r not in lost]
    # answer = n - len(new_lost)
    # for i in new_reserve:
    #     if i - 1 in new_lost:
    #         new_lost.remove(i - 1)
    #         answer += 1
    #     # elif i in lost:
    #     #     lost.remove(i)
    #     #     answer += 1
    #     elif i + 1 in new_lost:
    #         new_lost.remove(i + 1)
    #         answer += 1
    #     if len(new_lost) == 0:
    #         break

    # 프로그래머스 강의 풀이
    u = [1] * (n + 2)
    for i in lost:
        u[i] -= 1
    for i in reserve:
        u[i] += 1
    print(u)
    for i in range(1, n + 1):
        if u[i] == 0 and u[i + 1] == 2:
            u[i: i + 1] = [1, 1]
        if u[i] == 2 and u[i + 1] == 0:
            u[i: i + 1] = [1, 1]
    answer = [x for x in u[1: n + 1] if x > 0]
    return len(answer)


n = 5
lost = [2, 4]
reserve = [3]
print(solution(n, lost, reserve))
