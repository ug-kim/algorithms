def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    index_set = set()
    index_set.add(costs[0][0])

    answer = 0
    while len(index_set) != n:
        for i, cost in enumerate(costs):
            if cost[0] in index_set and cost[1] in index_set:
                continue
            if cost[0] in index_set or cost[1] in index_set:
                index_set.update([cost[0], cost[1]])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break

    return answer
