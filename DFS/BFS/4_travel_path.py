import copy

paths = []


def dfs(tickets, visited, current, path):
    if 0 not in visited:
        paths.append(path)
        return
    for i in range(len(tickets)):
        temp_current = current

        if visited[i] == 0 and temp_current == tickets[i][0]:
            temp_path = copy.deepcopy(path)
            temp_visited = copy.deepcopy(visited)
            temp_current = tickets[i][1]
            temp_path.append(temp_current)
            temp_visited[i] = 1
            dfs(tickets, temp_visited, temp_current, temp_path)


def solution(tickets):
    for i in range(len(tickets)):

        if tickets[i][0] == "ICN":
            visited = [0 for _ in range(len(tickets))]
            path = tickets[i]
            current = tickets[i][1]
            visited[i] = 1
            dfs(tickets, visited, current, path)

    paths.sort()

    return paths[0]
