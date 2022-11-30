import copy


def solution(cost, order):
    answer = 0
    # order.sort()
    # _order = copy.deepcopy(order)
    # for i in range(1, len(order)):
    #     _order[i][0] = order[i][0] - order[i - 1][0]
    # print(_order)

    # part 1
    order.sort()
    _order = [order[0]]
    for i, (m, n) in enumerate(sorted(order)[1:]):
        _order.append([m - order[i][0], n])

    # part 2
    stack = []
    for m, n in _order:
        while stack:
            _m, _n = stack[-1]
            if _m / _n < m / n:
                break
            stack.pop()
            m, n = m + _m, n + _n
        stack.append([m, n])

    # part 3
    for m, n in stack:
        p_prev = 0
        for t, p in cost:
            if m * t >= n:
                break
            answer += (n - m * t) * (p - p_prev)
            p_prev = p
    return answer


cost = [[0, 10], [50, 20], [100, 30], [200, 40]]
order = [[3, 50], [7, 200], [8, 200]]
sol = solution(cost, order)
print(sol)
