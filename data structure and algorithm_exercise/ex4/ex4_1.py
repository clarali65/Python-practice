# Solution1

ceramic_dict = {'gray': 1, 'red': 2, 'green': 3, 'blue': 4}
know_list = []
N = 5
def ceramic(ceramic_dict, N, known_list):
    if N == 1:
        return 1
    elif known_list[N] > 0:
        return known_list[N]
    else:
        res = 0
        n = 0
        for i in (for c in range(len(ceramic_dict)) if c <= N):
            n = 1 + ceramic(ceramic_dict, N - i, known_list)
            known_list[N - i] = n
        for j in known_list:
            res = res + known_list[j]
        return res


# Solution2
brick = [1, 2, 3, 4]
m = {}
def dfs(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 1 + dfs(N - 1)
    if N == 3:
        return 1 + dfs(N - 1) + dfs(N - 2)
    if N == 4:
        return 1 + dfs(N - 1) + dfs(N - 2) + dfs(N - 3)
    if dfs(N) in m:
        return m[dfs(N)]
    else:
        sum = 0
        for x in brick:
            sum = sum + dfs(N - x)
        return sum
N = int(input())
print(dfs(N))