def findJudge(N, trust):
    count = [0] * (N + 1)
    for i, j in trust:
        count[i] = count[i] - 1
        count[j] = count[j] + 1
    for k in count:
        if k == N - 1:
            return k
    return -1

N = int(input())
trust = eval(input())
print(findJudge(N,trust))