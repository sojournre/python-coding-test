def solution(levels):
    if len(levels) < 4:
        return -1
    answer = 0
    levels.sort(reverse=True)
    high = len(levels) // 4
    answer = levels[high - 1]
    return answer


levels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
solution1 = solution(levels)
print(solution1)
