import heapq


def solution(operations):
    answer = []
    for i in operations:
        # print(i)
        o = i.split()[0]
        v = i.split()[1]
        print(o, v)

        if o == 'I':
            heapq.heappush(o)
        elif o == 'D':
            if v == -1:
                heapq.heappop()

    return answer
