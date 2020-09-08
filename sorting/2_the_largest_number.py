def solution(numbers):
    all_zero = [0 for _ in range(len(numbers))]
    if all_zero == numbers:
        return "0"

    numbers = list(map(str, numbers))
    numbers.sort()

    def change_idx(numbers):
        index_list = []
        for i in range(len(numbers) - 1):
            first = numbers[i]
            second = numbers[i+1]

            if first+second > second+first:
                index_list.append(i)
                temp = second
                numbers[i+1] = first
                numbers[i] = temp

        if len(index_list) == 0:
            return True
        else:
            return False

    while True:
        bool_value = change_idx(numbers)
        if bool_value == True:
            break

    numbers.reverse()
    answer = "".join(numbers)
    return answer
