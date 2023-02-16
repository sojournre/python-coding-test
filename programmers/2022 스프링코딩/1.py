def solution(lotteries):
    answer = 0
    var = 0
    # a = list(enumerate(lotteries))
    for i, v in enumerate(lotteries):
        v.append(i + 1)
        print(i, v)
        print(v[0])
        print(v[1] + 1)
        percent = v[0] / (v[1] + 1) * 100
        print(percent)
        if percent >= 100:
            percent = 100
        v.append(percent)
    print(lotteries)

    # print(a)
    # print(a[1][1][2])
    # sorted_lotterires = sorted(a, key=lambda x: x[1][2])
    sorted_lotterires = sorted(lotteries, key=lambda x: (-x[4], -x[2]))
    print(sorted_lotterires)

    return sorted_lotterires[0][3]


lotteries = [[50, 100, 50], [100, 199, 100], [2, 200, 500]]
print(solution(lotteries))
