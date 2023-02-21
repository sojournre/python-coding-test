#
# Complete the 'maxLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#

def maxLength(a, k):
    # Write your code here
    left = 0
    right = 0
    curr_sum = a[0]
    max_len = 0
    while left <= right and right < len(a):
        if curr_sum <= k:
            max_len = max(max_len, right - left + 1)
            right += 1
            if right < len(a):
                curr_sum += a[right]
        else:
            curr_sum -= a[left]
            left += 1
    return max_len
