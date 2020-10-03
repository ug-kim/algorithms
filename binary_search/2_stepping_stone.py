def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    answer = 0
    left = 0
    right = distance

    while left <= right:
        mid = (left + right) // 2
        prev = 0
        min_val = 1000000001
        removed = 0

        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                removed += 1
            else:
                min_val = min(min_val, rocks[i] - prev)
                prev = rocks[i]

        if removed > n:
            right = mid - 1
        else:
            answer = min_val
            left = mid + 1

    return answer
