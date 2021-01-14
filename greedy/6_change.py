# 거스름돈
# 500원, 100원, 50원, 10원 무한히 존재할 때
# 거슬러 줘야하는 돈이 N원일 때
# 거슬러줘야 할 동전의 최소 개수 구하기
# N은 항상 10의 배수이다

# 나의 답
N = 1260


def solution(N):
    answer = 0
    change = [500, 100, 50, 10]
    for c in change:
        temp = N // c
        N -= temp * c
        answer += temp
    return answer


print(solution(N))

# 답안 예시
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
