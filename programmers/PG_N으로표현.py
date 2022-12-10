def solution(N, number):
    # s = [set() for _ in range(8)]
    # for i, x in enumerate(s, start=1):
    #     x.add(int(str(N) * i))
    # print(s)
    # for i in range(len(s)):
    #     for j in range(i):
    #         for op1 in s[j]:
    #             for op2 in s[i - j - 1]:
    #                 s[i].add(op1 + op2)
    #                 s[i].add(op1 - op2)
    #                 s[i].add(op1 * op2)
    #                 if op2 != 0:
    #                     s[i].add(op1 // op2)
    #     if number in s[i]:
    #         answer = i + 1
    #         break
    # else:
    #     answer = -1
    # return answer

    if number == 1:
        return 1
    set_list = []

    # 다른 사람의 풀이
    for cnt in range(1, 9):  # 1개부터 8개까지 확인
        partial_set = set()
        partial_set.add(int(str(N) * cnt))  # 이어 붙여서 만드는 경우 넣기
        for i in range(cnt - 1):  # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        # 만든 집합에 number가 처음 나오는지 확인
        if number in partial_set:
            return cnt
        set_list.append(partial_set)
    return -1


sol = solution(5, 12)
print(sol)