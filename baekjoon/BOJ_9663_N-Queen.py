# n = int(input())
#
#
# # Check if a queen can be placed at a given position
# def is_valid(board, row, col):
#     for r, c in board:
#         if c == col or r - c == row - col or r + c == row + col:
#             return False
#     return True
#
#
# # Recursive function to place queens on the board
# def place_queens(board, row):
#     if row == n:
#         return 1
#     count = 0
#     for col in range(n):
#         if is_valid(board, row, col):
#             board.append((row, col))
#             count += place_queens(board, row + 1)
#             board.pop()
#     return count
#
#
# # Call the recursive function to find the number of solutions
# print(place_queens([], 0))

N = int(input())

# Initialize a list to keep track of the positions of the queens
queens_pos = [-1] * N

# Initialize a variable to keep track of the number of solutions
count = 0


# Function to check if it is possible to place a queen at a given row and column
def is_possible(row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if queens_pos[i] == col or abs(queens_pos[i] - col) == row - i:
            return False
    return True


# Recursive function to place queens on the board
def place_queen(row):
    global count
    if row == N:
        # All queens have been placed, so we have found a solution
        count += 1
    else:
        for col in range(N):
            if is_possible(row, col):
                queens_pos[row] = col
                place_queen(row + 1)


# Start with the first row
place_queen(0)

# Print the number of solutions
print(count)
