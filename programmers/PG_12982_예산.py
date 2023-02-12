def solution(d, budget):
    # answer = 0
    # sum_amount = 0
    # d.sort()
    # for i in range(len(d)):
    #     sum_amount += d[i]
    #     if sum_amount > budget:
    #         return i
    # return len(d)

    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d, budget))
