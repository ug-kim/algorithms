spot = input()

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, - 1, 2, -2, 2, -2]

spots = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

n_spot = []

for i in range(len(spots)):
    if spot[0] == spots[i]:
        n_spot = [i + 1, int(spot[1])]
        break

answer = 0
for i in range(len(dx)):
    x = n_spot[0] + dx[i]
    y = n_spot[1] + dy[i]
    if x < 1 or x > 8 or y < 1 or y > 8:
        continue
    answer += 1

print(answer)
