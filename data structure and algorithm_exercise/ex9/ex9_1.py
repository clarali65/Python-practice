def canFinish(self,n,pre):
    clen = len(pre)
    if clen == 0:
        return True

    in_degrees=[0 for _ in range(n)]
    adj = [set() for _ in range(n)]
    for second,first in pre:
        in_degrees[second] = in_degrees[second] + 1
        adj[first].add(second)

    queue = []
    for i in range(n):
        if in_degrees[i] == 0:
            queue.append(i)

    counter = 0
    while queue:
        top = queue.pop(0)
        counter = counter + 1
        for successor in adj[top]:
            in_degrees[successor] = in_degrees[successor] - 1
            if in_degrees[successor] == 0:
                queue.append(successor)
    return counter == n

n=int(input())
pre=eval(input())
print(canFinish(n, pre))