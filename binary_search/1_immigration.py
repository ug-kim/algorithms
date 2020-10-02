def solution(n, times):
    high = n * max(times)
    low = 1
    answer = 0

    while low <= high:
        mid = (high + low) // 2
        people = 0
        for t in times:
            people += mid // t
            if people >= n:
                answer = mid
                high = mid - 1
                break
        else:
            low = mid + 1
    return answer
