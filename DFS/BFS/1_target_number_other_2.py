from itertools import product

numbers = [1, 1, 1, 1, 1]
target = 3


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    # product(*l)은 [(1, -1), (1, -1), (1, -1), (1, -1), (1, -1)]의 각각을 Cartesian Product한 결과
    # [(1, 1, 1, 1, 1), (1, 1, 1, 1, -1), (1, 1, 1, -1, 1), (1, 1, 1, -1, -1), ... ,(-1, -1, -1, -1, 1), (-1, -1, -1, -1, -1)]
    # map(sum, product(*l))은 product(*l)의 리스트 안의 tuple들의 합을 리스트로 나열해서 보여준다
    s = list(map(sum, product(*l)))
    return s.count(target)


print(solution(numbers, target))
