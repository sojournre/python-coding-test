def solution(people, tshirts):
    answer = 0
    people.sort()
    tshirts.sort()
    p, t = 0, 0
    while p < len(people) and t < len(tshirts):
        if people[p] <= tshirts[t]:
            p += 1
            answer += 1
        t += 1
    return answer


people = [2, 3]
tshirts = [1, 2, 3]
sol = solution(people, tshirts)
print(sol)
