import string


def solution(name):
    a = string.ascii_uppercase
    a = list(a)
    ascii_len = len(a)

    count = 0
    a_count = 0
    before = '!'
    not_a_idx = 0
    for i, n in enumerate(name):
        if i != 0:
            count += 1

        idx = a.index(n)
        temp = ascii_len - idx
        if idx < temp:
            count += idx
        else:
            count += temp

        if before == 'A' and n == 'A':
            a_count += 1
        elif n == 'A':
            not_a_idx = i - 1
            a_count += 1

        if before == 'A' and n != 'A':
            if not_a_idx == -1:
                count -= a_count - 1
            elif not_a_idx + 1 <= a_count:
                count -= a_count - (not_a_idx + 1) + 1
            a_count = 0

        before = n

    return count
