def solution(reference, track):
    answer = 0
    r_idx = 0
    t_idx = 0
    jump = 0

    while t_idx < len(track):
        if reference[r_idx] != track[t_idx]:
            r_idx += 1
        else:
            r_idx += 1
            t_idx += 1
            jump += 1
            if r_idx == len(reference):
                answer = jump
                jump = 0
                r_idx = 0
    return answer


reference = "abc"
track = "bcab"
# solution(reference, track)
print(solution(reference, track))
