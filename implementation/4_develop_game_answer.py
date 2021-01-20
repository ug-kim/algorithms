N, M = map(int, input().split())

# 방문한 위치 저장하기 위한 맵 생성해 0으로 초기화
d = [[0] * M for _ in range(N)]
# 현재 캐릭터의 X좌표, Y좌표, 방향 입력받기
x, y, turn = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))


# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global turn
    turn -= 1
    if turn == -1:
        turn = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[turn]
    ny = y + dy[turn]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and maps[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없가나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[turn]
        ny = x - dy[turn]
        # 뒤로 갈 수 있다면 이동
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
