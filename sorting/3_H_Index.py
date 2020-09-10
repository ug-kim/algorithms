def solution(citations):
    n = len(citations)

    citations.sort(reverse=True)

    answer = 0
    for i in range(n):
        answer += 1
        c = citations[i]
        if answer > c:
            answer -= 1
            break

    return answer
