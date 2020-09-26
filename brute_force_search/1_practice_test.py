def solution(answers):
    answer = []
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    supo_count = [0 for _ in range(3)]

    for i in range(len(answers)):
        if answers[i] == supo_1[i % 5]:
            supo_count[0] += 1
        if answers[i] == supo_2[i % 8]:
            supo_count[1] += 1
        if answers[i] == supo_3[i % 10]:
            supo_count[2] += 1

    max_count = max(supo_count)
    for i in range(3):
        if supo_count[i] == max_count:
            answer.append(i + 1)

    return answer
