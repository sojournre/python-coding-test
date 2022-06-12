def solution(p):
    answer = [0] * len(p)
    i = 0
    while i < len(p):
        min_value = min(p[i:])
        j = p.index(min_value)
        print(min_value, j)

        if i != j:
            p[i], p[j] = p[j], p[i]
            answer[i] = answer[i] + 1
            answer[j] = answer[j] + 1
        i = i + 1

    print(p)
    print(answer)

    return answer


p = [2, 5, 3, 1, 4]
# p = [2, 3, 4, 5, 6, 1]
solution(p)
