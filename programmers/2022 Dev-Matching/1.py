def solution(grade):
    answer = 0
    grade_sort = sorted(grade)

    for i in range(len(grade)):
        if grade[i] > grade_sort[i]:
            answer += grade[i] - grade_sort[i]
    return answer


grade = [2, 1, 3]  # result = 1
solution(grade)
solution([1, 2, 3])  # 0
solution([3, 2, 3, 6, 4, 5])  # 3

# 2, 1, 3
# 1, 2, 3
# 1
#
# 3, 2, 3, 6, 4, 5
# 2, 3, 3, 4, 5, 6
# 1,       2
