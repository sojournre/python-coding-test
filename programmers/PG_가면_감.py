def solution(reply):
    answer = 0
    r = list(enumerate(reply))
    # for i, v in enumerate(reply):
    #     r[i].append(v)
    print(r)
    return answer


reply = [[0], [8], [1, 3], [2], [1], [1, 4, 6], [2, 5], [3, 6], [4]]
sol = solution(reply)
print(sol)