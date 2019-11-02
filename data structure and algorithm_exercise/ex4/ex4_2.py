def candy(ratings):
    candy_list = []
    n = len(ratings)
    if n == 0:
        return 0

    for i in range(n):
        if i == 0:
            candy_list[i] = 1
        else:
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1
            else:
                candy_list[i] = 1
    for i in range(n, -1, -1):
        if i == n:
            continue
        else:
            if ratings[i] > ratings[i + 1]:
                candy_list[i] = max(candy_list[i], ratings[i + 1] + 1)
            else:
                continue
    res = sum(candy_list)
    return res

lst = eval(input())
print(candy(lst))