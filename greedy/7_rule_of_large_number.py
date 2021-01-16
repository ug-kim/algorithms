N, M, K = map(int, input().split())
inputs = list(map(int, input().split()))

inputs.sort(reverse=True)

first = inputs[0]
second = inputs[1]

# 나의 풀이
# M이 < 10,000 이므로 이 방식으로 가능하지만,
# 크기가 100억 이상 커지면 시간 초과 판정 받을 것이다

count = 0
answer = 0
for _ in range(M):
    if count == K:
        count = 0
        answer += second
    else:
        answer += first
        count += 1

print(answer)  # return


# 시간 복잡도 줄이는 풀이
# 반복되는 수열에 대해서 파악하기

temp_1 = M // (K + 1)
temp_2 = M % (K + 1)
answer = first * (temp_1 * K + temp_2) + second * temp_1

print(answer)  # return
