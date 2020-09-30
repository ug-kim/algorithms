from collections import defaultdict, deque


def solution(n, vertex):
    graph = defaultdict(set)

    for start, end in vertex:
        graph[start].add(end)
        graph[end].add(start)

    queue = deque([(1, 0)])
    visited = [-1]*(n + 1)

    while queue:
        n, depth = queue.popleft()
        visited[n] = depth
        for i in graph[n]:
            if visited[i] == -1:
                visited[i] = 0
                queue.append((i, depth + 1))

    return visited.count(max(visited))
