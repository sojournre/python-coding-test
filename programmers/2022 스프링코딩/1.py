def solution(lotteries):
    answer = 0
    a = list(enumerate(lotteries))
    # for i, v in enumerate(lotteries):
    #     print(i, v)
    #     # print(v[0])
    #     # print(v[1] + 1)
    #     # var = v[1]
    #     if var >= 100:
    #         var = 100
    #     lotteries.append(var)
    # print(lotteries)

    # print(a)
    # print(a[1][1][2])
    # sorted_lotterires = sorted(a, key=lambda x: x[1][2])
    sorted_lotterires = sorted(a, key=lambda x: (-x[1][0] / (x[1][1]+1) * 100, -x[1][2]))
    print(sorted_lotterires)

    return sorted_lotterires[0][0] + 1


lotteries = [[50, 1, 50], [100, 199, 100], [2, 1, 500]]
print(solution(lotteries))
