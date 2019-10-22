# solution1
temp = 999999
res_list = [1, 3]
num = int(input())
def hanoi4():
    if num == 0:
        print(0)
    else:
        for n in range(2, num):
            res_list.append(temp)
            for x in range(0, n):
                if (2 * res_list[x] + 2 ** (n - x) - 1) < res_list[n]:
                    res_list[n] = 2 * res_list[x] + 2 ** (n - x) - 1
        print(res_list[num - 1])
hanoi4()

# solution2
def hanoi4(n):
    h_list = [0] * (n + 1)

    def f(m):
        if h_list[m]:
            return h_list[m]
        res = 2 ** m - 1
        for x in range(1, m):
            res = min(res, 2 * f(x) + 2 ** (m - x) - 1)
        h_list[m] = res
        return res
    return f(n)
print(hanoi4(int(input())))