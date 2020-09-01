from collections import deque


def solution(begin, target, words):
    queue = deque()
    bfs_dict = dict()

    def trans_available_func(a, b): return sum(
        (1 if x != y else 0) for x, y in zip(a, b)) == 1

    bfs_dict[begin] = set(
        filter(lambda x: trans_available_func(begin, x), words))

    for word in words:
        bfs_dict[word] = set(
            filter(lambda x: trans_available_func(word, x), words))

    queue.append((begin, 0))

    while queue:
        current, depth = queue.popleft()

        if depth > len(words):
            return 0

        for w in bfs_dict[current]:
            if w == target:
                return depth + 1
            else:
                queue.append((w, depth+1))

    return 0
