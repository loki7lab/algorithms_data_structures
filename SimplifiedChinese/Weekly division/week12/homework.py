#*********************1*********************
def canFinish(n, pre):
    if n == 0:
        return False
    graph = [[] for _ in range(n)]
    for sub in pre:
        graph[sub[1]].append(sub[0])

    def isCircle(N):
        visited.append(N)
        if N in path:
            return True
        path.append(N)
        keys = graph[N]
        if keys == []:
            return False
        for key in keys:
            if key in visited and key not in path:
                continue
            if isCircle(key):
                return True
            path.pop()
        else:
            return False

    i = 0
    while i < n:
        visited = []
        path = []
        if isCircle(i):
            return False
        i += 1
    else:
        return True


n = int(input())
pre = eval(input())
print(canFinish(n, pre))
#***************2********************
def netSum():
    x_list = [0] * len(list)
    y_list = [0] * len(list[0])
    count = 0
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j] == 1:
                x_list[i] += 1
                y_list[j] += 1
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j] == 1:
                if x_list[i] >= 2 or y_list[j] >= 2:
                    count += 1

    return count


list = eval(input())
print(netSum())
