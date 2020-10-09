from collections import deque


def solution(people, limit):
    answer = 0
    poo = sorted(people)
    poo = deque(poo)
    while poo:
        if len(poo) == 1:
            answer += 1
            break
        if poo[0] + poo[-1] > limit:
            poo.pop()
            answer += 1
        else:
            poo.popleft()
            poo.pop()
            answer += 1
    return answer
