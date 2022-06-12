def solution(periods, payments, estimates):
    answer = [0, 0]
    this_vip = [0] * len(periods)
    next_vip = [0] * len(periods)
    for i in range(len(periods)):
        this_sum = sum(payments[i])
        next_sum = sum(payments[i][1:]) + estimates[i]
        if (periods[i] >= 24 and this_sum >= 900000) or (periods[i] >= 60 and this_sum >= 600000):
            this_vip[i] = 1
        if (periods[i] + 1 >= 24 and next_sum >= 900000) or (periods[i] + 1 >= 60 and next_sum >= 600000):
            next_vip[i] = 1

    for i in range(len(this_vip)):
        if this_vip[i] == 0 and next_vip[i] == 1:
            answer[0] = answer[0] + 1
        if this_vip[i] == 1 and next_vip[i] == 0:
            answer[1] = answer[1] + 1

    return answer


periods = [20, 23, 24]
payments = [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
           [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
           [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]
estimates = [100000, 100000, 100000]

l = solution(periods, payments, estimates)
print(l)
