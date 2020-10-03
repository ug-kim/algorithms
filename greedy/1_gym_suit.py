def solution(n, lost, reserve):
    student = [i for i in range(1, n + 1)]
    union = set(reserve) & set(lost)

    reserve = set(reserve) - union
    lost = set(lost) - union
    in_class = len(set(student) - set(lost))

    for l in lost:
        if (l - 1) in reserve:
            reserve.remove(l - 1)
            in_class += 1
        elif (l + 1) in reserve:
            reserve.remove(l + 1)
            in_class += 1

    return in_class
