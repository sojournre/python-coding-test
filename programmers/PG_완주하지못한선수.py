def solution(participant, completion):
    # 나의 풀이
    # answer = ''
    # for name in completion:
    #     if name in participant:
    #         participant.remove(name)
    # return participant[0]

    # participant.sort()
    # completion.sort()
    #
    # for i in range(len(completion)):
    #     if participant[i] != completion[i]:
    #         return participant[i]
    # return participant[-1]

    # 해시를 이용한 풀이
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1

    for x in completion:
        d[x] -= 1

    dnf = [k for k, v in d.items() if v > 0]
    return dnf[0]
