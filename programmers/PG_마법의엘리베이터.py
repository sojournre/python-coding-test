def solution(storey):
    # answer = 0
    # s = str(storey)
    # for i, v in enumerate(s[::-1]):
    #     print(i, v)
    #     v = int(v)
    #     if v > 5:
    #         answer += 10 * (i + 1) - v
    #         s[i + 1] += 1
    #     else:
    #         answer += v
    # return answer

    if storey <= 1:
        return storey
    q, r = divmod(storey, 10)
    return min(solution(q) + r, solution(q + 1) + (10 - r))


sol = solution(2554)
print(sol)
