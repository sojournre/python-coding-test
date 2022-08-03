import collections


def solution(gems):
    t = set(gems)
    need = collections.Counter(t)
    missing = len(t)
    left = start = end = 0

    # 오른쪽 포인터 이동
    for right, char in enumerate(gems, 1):
        missing -= need[char] > 0
        need[char] -= 1

        if missing == 0:
            while left < right and need[gems[left]] < 0:
                need[gems[left]] += 1
                left += 1

            if not end or right - left < end - start:
                start, end = left, right
                need[gems[left]] += 1
                missing += 1
                left += 1
    return [start + 1, end]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
