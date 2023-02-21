#
# Complete the 'getFinalString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def getFinalString(s):
    # Write your code here
    while "AWS" in s:
        s = s.replace("AWS", "")
    if s == "":
        return "-1"
    return s


print(getFinalString("ABCDWS"))