N = int(input())
direction = input().split()


def cal_dir(direction, spot):
    new_spot = spot[:]
    if direction == "R":
        new_spot[1] += 1
    elif direction == "L":
        new_spot[1] -= 1
    elif direction == "U":
        new_spot[0] -= 1
    elif direction == "D":
        new_spot[0] += 1
    return new_spot


def is_correct(spot):
    if spot[0] > 0 and spot[0] <= N and spot[1] > 0 and spot[1] <= N:
        return True
    else:
        return False


spot = [1, 1]

for d in direction:
    n_spot = cal_dir(d, spot)
    if is_correct(n_spot):
        spot = n_spot

print(spot[0], spot[1])
