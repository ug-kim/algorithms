def solution(n, results):
    answer = 0
    graph = [[0 for cols in range(n)] for rows in range(n)]

    for x, y in results:
        graph[x-1][y-1] = 1
        graph[y-1][x-1] = -1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                for m in range(n):
                    if graph[j][m] == 1 and graph[i][m] == 0:
                        graph[i][m] = 1
                        graph[m][i] = -1
            elif graph[i][j] == -1:
                for m in range(n):
                    if graph[j][m] == -1 and graph[i][m] == 0:
                        graph[i][m] = -1
                        graph[m][i] = 1

    print(graph)
    for i in range(n):
        # 자기 자신만 0이어야 한다
        if graph[i].count(0) == 1:
            answer += 1

    return answer
