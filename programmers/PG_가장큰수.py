def solution(numbers):
    answer = ''
    # s = list(map(str, numbers))
    # print(s)
    # s.sort(key=lambda x: x * 3, reverse=True)
    # # print(s)
    # # print('333' > '303030')
    # answer = "".join(s)

    # 프로그래머스 풀이
    numbers = [str(x) for x in numbers]
    print(numbers)
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    print(numbers)
    return answer


sol = solution([3, 30, 34, 5, 9])
print(sol)
