from heapq import heappop, heappush


def solution(t, k, study, pstudy):
    # answer = 0
    # s = list(enumerate(study))
    # p = list(enumerate(pstudy))
    # p = sorted(p, key=lambda x: x[1])
    # i = 0
    # time = 0
    # for _ in range(k):
    #     time += p[i][1]
    #     s.
    #     i += 1
    # print(s)
    # return answer

    visited = [0] * len(study)
    diff = [0] * k
    study_hq = [(s, i) for i, s in enumerate(study)]
    paper_hq = [(p, i) for i, p in enumerate(pstudy)]
    study_hq.sort()
    paper_hq.sort()
    sidx, pidx = 0, 0

    while sidx < len(study):
        if diff[0] + paper_hq[pidx][0] < study_hq[sidx][0]:
            c, i = paper_hq[pidx]
            c += diff[0]
            heappop(diff)
            heappush(diff, study[i] - pstudy[i])
        else:
            c, i = study_hq[sidx]

        if c > t:
            break

        t -= c
        visited[i] = 1

        while sidx < len(study) and visited[study_hq[sidx][1]]:
            sidx += 1
        while pidx < len(study) and visited[paper_hq[pidx][1]]:
            pidx += 1

    return sum(visited)


t = 10
k = 2
study = [8, 13, 8, 9, 5]
pstudy = [1, 3, 4, 7, 4]
sol = solution(t, k, study, pstudy)
print(sol)
