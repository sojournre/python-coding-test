def solution(sizes):
    answer = 0
    w_list = h_list = []

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            w_list.append(sizes[i][0])
            h_list.append(sizes[i][1])
        else:
            w_list.append(sizes[i][1])
            h_list.append(sizes[i][0])
        # sizes[i].sort(reverse=True)
    # print(sizes)
    w = max(w_list)
    h = max(h_list)
    return w * h
