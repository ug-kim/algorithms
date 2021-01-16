N, M = map(int, input().split())

before = 0
answer = 0
for _ in range(N):
    inputs = list(map(int, input().split()))
    min_val = min(inputs)

    # 나의 답안
    if min_val > before:
        answer = min_val
    before = min_val

    # 제시 답안
    answer = max(answer, min_val)

print(answer)
