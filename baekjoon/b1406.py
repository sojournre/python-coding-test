import sys

left = list(sys.stdin.readline().strip().lower())

right = []

N = int(sys.stdin.readline().strip())
for i in range(N):
    command = sys.stdin.readline().strip()

    if command == "L" and left:
        right.append(left.pop())

    elif command == "D" and right:
        left.append(right.pop())

    elif command == "B" and left:
        left.pop()

    elif command[0] == "P":
        left.append(command[2])

print(left)
print(right)

print("".join(left + right[::-1]))
