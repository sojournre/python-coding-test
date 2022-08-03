import sys

input = sys.stdin.readline
N = int(input())
solution = list(map(int, input().split()))

solution.sort()

# 투 포인터 지정
left = 0
right = N - 1

# 초기값 설정
answer = abs(solution[left] + solution[right])
final = [solution[left], solution[right]]

while left < right:
    s_left = solution[left]
    s_right = solution[right]

    total = s_left + s_right

    if abs(total) < answer:
        answer = abs(total)
        final = [s_left, s_right]
        if answer == 0:
            break

    if total < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
