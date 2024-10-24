#*************1**************
def findJudge(N):
    trust_list = [0] * (N + 1)
    trusted_list = [0] * (N + 1)
    for i, j in trust:
        trust_list[i] += 1
        trusted_list[j] += 1
    count = 0
    result = []
    for i in range(1, N + 1):
        if trust_list[i] == 0 and trusted_list[i] == N - 1:
            count += 1
            result.append(i)
    if count == 1:
        return result[0]
    else:
        return -1


N = int(input())
trust = eval(input())
print(findJudge(N))

#****************2***********************
grid = eval(input())
M = len(grid)
N = len(grid[0])
dist = [[None for _ in range(M)] for _ in range(N)]
queue = []
for i in range(M):
    for j in range(N):
        if grid[i][j]:
            queue.append((i, j))
            dist[i][j] = 0
if queue == [] or len(queue) == M * N:
    print(-1)
else:
    while queue:
        x, y = queue.pop(0)
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < M and 0 <= j < N and dist[i][j] == None:
                dist[i][j] = dist[x][y] + 1
                queue.append((i, j))
    print(max(max(row) for row in dist))

#*********************3**********************
def canVisitAll(n):
    visited.append(n)
    keys = rooms[n]
    for key in keys:
        if key not in visited:
            canVisitAll(key)
    return


rooms = eval(input())
N = len(rooms)
visited = []
canVisitAll(0)
if len(visited) == N:
    print(True)
else:
    print(False)
