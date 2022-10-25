def solution(s):
    answer = 0
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
            answer = max(answer, int(s[i:i + 3]))

    if answer == 0:
        answer = -1
    if answer == "000":
        answer = 0

    return answer


s = "12333"
i = solution(s)
print(i)
