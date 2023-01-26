import sys

input = sys.stdin.readline


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    global count, result
    i = low
    j = mid + 1
    t = 1
    tmp = []

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            ans.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            ans.append(arr[j])
            j += 1

    while i <= mid:
        # tmp[t] = arr[i]
        tmp.append(arr[i])
        ans.append(arr[i])
        i += 1
        # t += 1

    while j <= high:
        # tmp[t] = arr[j]
        tmp.append(arr[j])
        ans.append(arr[j])
        j += 1
        t += 1

    i = low
    t = 0
    while i <= high:
        arr[i] = tmp[t]
        # count += 1
        # if count == k:
        #     result = arr[i]
        #     break
        i += 1
        t += 1


n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
result = -1
ans = []
merge_sort(arr, 0, n - 1)
# print(ans)
# print(result)
if len(ans) < k:
    print(-1)
else:
    print(ans[k - 1])
