def solution(array, commands):
    answer = []
    for start, end, idx in commands:
        start -= 1
        temp = array[start:end]
        temp.sort()
        answer.append(temp[idx-1])

    return answer
