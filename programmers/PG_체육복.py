def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    new_lost = [l for l in lost if l not in reserve]
    new_reserve = [r for r in reserve if r not in lost]
    answer = n - len(new_lost)
    for i in new_reserve:
        if i - 1 in new_lost:
            new_lost.remove(i - 1)
            answer += 1
        # elif i in lost:
        #     lost.remove(i)
        #     answer += 1
        elif i + 1 in new_lost:
            new_lost.remove(i + 1)
            answer += 1
        if len(new_lost) == 0:
            break
    return answer


n = 10
lost = [1, 2, 3, 4, 5, 7]
reserve = [1, 2, 4, 5, 7]
print(solution(n, lost, reserve))
