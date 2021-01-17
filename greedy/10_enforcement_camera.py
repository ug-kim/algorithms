def solution(routes):

    routes.sort(key=lambda x: x[1])
    prev_camera = -30000

    answer = 0

    for r in routes:
        if prev_camera < r[0]:
            answer += 1
            prev_camera = r[1]

    return answer
