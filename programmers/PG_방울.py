from itertools import accumulate


def solution(bell):
    # answer = 0
    # for i in range(len(bell)):
    #     if bell[i] == 1:
    #         bell[i] = -1
    #     else:
    #         bell[i] = 1
    # print(bell)
    # sums = [0]
    # for i in range(len(bell)):
    #     sums.append(bell[i] + sums[i])
    # print(sums)
    coors_start = {}
    coors_end = {}
    for i, x in enumerate(accumulate([0] + [-1 if b == 1 else 1 for b in bell])):
        if x not in coors_start:
            coors_start[x] = i
        coors_end[x] = i
    return max(coors_end[x] - coors_start[x] for x in coors_end)


sol = solution([1, 2, 1, 1, 1, 2, 2, 1])
print(sol)
