# -를 만나면  -를 다시 만나기 전까지 +를 모두 괄호로 묶는다.
# 즉, - 값을 최대로 만들면 연산의 최소값을 구할수 있다.

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]

print(n)
