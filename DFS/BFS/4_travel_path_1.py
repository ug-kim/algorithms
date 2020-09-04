from collections import defaultdict


def dfs(graph, N, key, footprint):
    print("footprint: ", footprint)

    if len(footprint) == N + 1:
        return footprint

    # graph[key]가 없으면, 빈 list return
    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        temp = footprint[:]
        temp.append(country)

        ret = dfs(graph, N, country, temp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):

    answer = []

    N = len(tickets)

    graph = defaultdict(list)

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    print("graph: ", graph)

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer
