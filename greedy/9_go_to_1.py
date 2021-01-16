N, K = map(int, input().split())

# 나의 답안
answer = 0
while True:
    if N == 1:
        break
    if N % K == 0:
        answer += 1
        N = N // K
    else:
        answer += 1
        N -= 1

print(answer)

# N이 엄청 큰 수이면,
# N을 K로 최대한 나눈 후 1씩 계속 빼는 것이 비효율적이다

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (N // K) * K
    answer += (N - target)
    N = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break
    # K로 나누기
    answer += 1
    N //= K

# 마지막으로 남은 수에 대해 1씩 빼기
answer += (N - 1)
print(answer)
