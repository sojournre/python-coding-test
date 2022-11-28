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
    collected = []
    for i, v in enumerate(number):
        # print(i, v)
        while len(collected) > 0 and collected[-1] < v and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += number[i:]
            break
        collected.append(v)
    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer


sol = solution("1231234", 3)
print(sol)
