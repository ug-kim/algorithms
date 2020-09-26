from itertools import permutations
import math


def solution(numbers):
    def is_the_number(num):
        if num == 0 or num == 1:
            return False

        bound = int(math.sqrt(num))

        for i in range(2, bound + 1):
            if num % i == 0:
                return False
        return True

    count = 0

    num_list = []
    for i in range(len(numbers)):
        number_list = list(permutations(numbers, i + 1))
        number_list = [int(''.join(number)) for number in number_list]
        num_list.extend(number_list)

    num_list = list(set(num_list))

    for num in num_list:
        if is_the_number(num) == True:
            count += 1

    return count
