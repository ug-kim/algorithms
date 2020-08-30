def solution(n, computers):
    visited = [0 for _ in range(n)]
    paths = set()
    path = []

    def dfs(i):
        visited[i] = 1
        path.append(i)
        for j in range(0, n):
            if computers[i][j] == 1 and visited[j] == 0:
                dfs(j)

    for i in range(n):
        if visited[i] == 0:
            path = []
            dfs(i)
            path.sort()
            paths.add(''.join(map(str, path)))

    return len(paths)
