def maxDistance(grid):
    n, m = len(grid), len(grid[0])
    dist = [[float('inf') for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = []
    # 陆地计数
    cnt = 0
    ans = 0
    tot = n * m
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                dist[i][j] = 0
                visited[i][j] = True
                q.append((i, j))
                cnt = cnt + 1
    if cnt == tot or cnt == 0:
        return -1
    while q:
        x, y = q.pop(0)
        for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= i < n and 0 <= j < m and not visited[i][j]:
                dist[i][j] = min(dist[i][j], dist[x][y]+1)
                ans = max(ans, dist[i][j])
                visited[i][j] = True
                q.append((i, j))
    return ans

grid = eval(input())
print(maxDistance(grid))


# DFS
def canVisitAll(rooms):
    room_map = {0}
    def enterroom(keys):
        for key in keys:
            if key not in room_map:
                room_map.add(key)
                enterroom(rooms[key])
            else:
                pass
        return
    enterroom(rooms[0])
    return len(room_map) == len(rooms)

rooms = eval(input())
print(canVisitAll(rooms))