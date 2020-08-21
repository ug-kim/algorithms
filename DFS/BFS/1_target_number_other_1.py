numbers = [1, 1, 1, 1, 1]
target = 3


def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:  # not numbers는 numbers가 비었을 때 true
        return 0
    else:
        # solution 함수 실행 결과값을 더해주지만, 결국 solution 함수는 각각 재귀함수로 실행된 후 더해진다
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


print(solution(numbers, target))
