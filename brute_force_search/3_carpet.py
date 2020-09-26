def solution(brown, yellow):
    def find_list(yellow):
        candi_list = []

        if yellow == 1:
            return [[1, 1]]

        for i in range(1, int(yellow/2) + 1):
            width = int(yellow / i)
            if width < i:
                break
            if yellow % i == 0:
                candi_list.append([width, i])

        return candi_list

    candi_list = find_list(yellow)

    for width, height in candi_list:
        temp_brown = width * 2 + height * 2 + 4

        if temp_brown == brown:
            return [width + 2, height + 2]
