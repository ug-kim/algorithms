def solution(number, k):
    stack = []
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue

        is_finish = False
        while stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
            if k == 0:
                stack.extend(list(number[i:]))
                is_finish = True
                break

        if is_finish:
            break

        stack.append(number[i])

    if k != 0:
        stack = stack[:len(stack) - k]
        # stack = stack[:-k]

    answer = "".join(stack)
    return answer
