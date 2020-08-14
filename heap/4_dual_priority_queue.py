heap = []


def insert_value(value):
    value = int(value)
    if len(heap) == 0:
        heap.append(value)
        return 0

    for i in range(len(heap)):
        if value <= heap[i]:
            heap.insert(i, value)
            return

    heap.append(value)


def solution(operations):
    for operation in operations:
        inst, value = operation.split(" ")
        if inst == "I":
            insert_value(value)
        elif inst == "D":
            if len(heap) == 0:
                continue

            if value == "1":
                heap.pop()
            elif value == "-1":
                heap.pop(0)

    if len(heap) == 0:
        return [0, 0]
    elif len(heap) == 1:
        temp = heap[0]
        return [temp, temp]
    else:
        min = heap[0]
        max = heap[-1]
        return [max, min]
