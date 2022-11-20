def solution(participant, completion):
#     나의 풀이
#     answer = ''
#     for name in completion:
#         if name in participant:
#             participant.remove(name)
#     return participant[0]

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
