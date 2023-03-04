import itertools


def solution(letters, k):
    if k > len(letters):
        return ""
    combinations = itertools.combinations(letters, k)
    sorted_combinations = sorted(combinations)
    print(sorted_combinations)
    return ''.join(sorted_combinations[-1])


letters = "zbgaj"
k = 3
print(solution(letters, k))
