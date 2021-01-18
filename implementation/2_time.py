N = int(input())

# 나의 풀이


def is_three(num):
    strings = list(str(num))
    if '3' in strings:
        return True
    else:
        return False


answer = 0

for i in range(N + 1):
    if is_three(i):
        answer += (60 * 60)
        continue
    for j in range(60):
        if is_three(j):
            answer += 60
            continue
        for k in range(60):
            if is_three(k):
                answer += 1
print(answer)

# 정답 풀이

answer = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                answer += 1

print(answer)
