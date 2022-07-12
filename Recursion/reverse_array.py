from operator import le


def reverse_arr(left_idx, elem):
    if left_idx >= len(elem) // 2:
        return
    right_idx = len(elem) - 1 - left_idx
    elem[left_idx], elem[right_idx] = elem[right_idx], elem[left_idx]
    reverse_arr(left_idx + 1, elem)

elem = input().split()
reverse_arr(0, elem)

print(' '.join(elem))