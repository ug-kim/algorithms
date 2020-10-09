import heapq


def solution(n, costs):
    answer = 0
    from_to = list(list() for _ in range(n))

    visited = [False] * n
    priority = []

    for a, b, cost in costs:
        from_to[a].append((b, cost))
        from_to[b].append((a, cost))

    heapq.heappush(priority, (0, 0))

    while False in visited:
        cost, start = heapq.heappop(priority)  # for min heap
        if visited[start]:
            continue

        visited[start] = True
        answer += cost
        for end, cost in from_to[start]:
            if visited[end]:
                continue
            else:
                heapq.heappush(priority, (cost, end))

    return answer
