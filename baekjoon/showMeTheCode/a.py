n = int(input())
stone = list(map(int, input().split()))
left_gold = 0
right_gold = 0
count = 0
ans = 0

for i in range(1, n):
    if stone[i - 1] == stone[i]:
        if count == 0:
            if stone[i] == 1:
                left_gold += 2
            else:
                right_gold += 2
        else:
            if stone[i] == 1:
                left_gold += 1
            else:
                right_gold += 1
        count += 1
    else:
        count = 0

if left_gold == 0 and right_gold == 0:
    left_gold = 1
# elif left_gold == 0:
#     right_gold += 1
# elif right_gold == 0:
#     left_gold += 1r

ans = abs(left_gold - right_gold)

print(ans)
