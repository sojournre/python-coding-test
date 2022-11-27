from itertools import combinations


def solution(number, k):
    answer = ''
    # l = list(combinations(number, len(number) - k))
    # combi = []
    # print(l)
    # for i in l:
    #     join = "".join(i)
    #     combi.append(int(join))
    # print(combi)
    # answer = max(combi)
    # return str(answer)
    for i in number:
        print(i)

    return answer


sol = solution("1924", 2)
print(sol)
