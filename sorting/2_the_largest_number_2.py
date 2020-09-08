from functools import cmp_to_key


def comparator(a, b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution(numbers):
    n = map(str, numbers)
    n = sorted(n, key=cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer
