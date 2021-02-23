from collections import defaultdict

# 아이디어
# 1. 도달할 수 없는 경우 set 무조건 정답에 포함
# 2. 도달할 수 없는 경우에서 그래프 타고 갔을 때 말고, 포함 안된 집합도 정답에 포함 -> 필요 없음
# 2번의 경우 그래프 타고 갔을 때 도달할 수 없으면 결국 1번이기 때문에
# 1번만 고려해주면 된다


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes_set = set([i for i in range(n)])
        graph = defaultdict(set)

        for edge in edges:
            graph[edge[0]].add(edge[1])

        # print(graph.values()) # dict_values([{1, 2}, {5}, {4}, {2}])

        graph_values = graph.values()
        g_values = set()
        for v in graph_values:
            if len(v) == 1:
                g_values.add(list(v)[0])
            else:
                g_values.update(v)
        # print(g_values) # {1, 2, 4, 5}

        answer_set = set()
        answer_set = nodes_set - g_values
        # print(answer_set)
        return list(answer_set)

        # DFS
        # visited = set()
        # stack = list(answer_set)
        # while stack:
        #     n = stack.pop()
        #     if n not in visited:
        #         visited.add(n)
        #         stack += graph[n] - visited

        # visited_set = set(visited)
        # left_one = nodes_set - (answer_set | visited_set)
        # answer_set = answer_set | left_one

        # answer = list(answer_set)
        # return answer
