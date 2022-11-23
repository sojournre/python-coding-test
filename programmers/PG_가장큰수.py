def solution(numbers):
    answer = ''
    s = list(map(str, numbers))
    # print(s)
    s.sort(key=lambda x: x * 3, reverse=True)
    # print(s)
    # print('333' > '303030')
    answer = "".join(s)
    return answer


sol = solution([3, 30, 34, 5, 9])
print(sol)
