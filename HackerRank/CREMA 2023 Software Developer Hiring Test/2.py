#
# Complete the 'findRange' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER num as parameter.
#

def findRange(num):
    # Write your code here
    num_str = str(num)
    max_num = num_str
    min_num = num_str
    for i, digit in enumerate(num_str):
        for j in range(10):
            if j != int(digit):
                new_num = num_str.replace(digit, str(j))
                if new_num[0] != '0' and new_num > max_num:
                    max_num = new_num
                if new_num[0] != '0' and new_num < min_num:
                    min_num = new_num
    print(max_num, min_num)
    return int(max_num) - int(min_num)