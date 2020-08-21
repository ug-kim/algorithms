answer = 0

# 전형적인 dfs 방법


def dfs(numbers, target, idx, start):
    if idx == len(numbers) and start == target:
        global answer
        answer += 1

    if idx == len(numbers):
        return

    # numbers, target을 넘겨준 건 전역변수가 아니라 solution 함수 인자이기 때문
    dfs(numbers, target, idx+1, start + numbers[idx])
    dfs(numbers, target, idx+1, start - numbers[idx])


def solution(numbers, target):
    dfs(numbers, target, 0, 0)

    return answer
