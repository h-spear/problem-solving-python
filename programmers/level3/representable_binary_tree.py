# https://school.programmers.co.kr/learn/courses/30/lessons/150367


def left_child(i, height):
    return i - 2 ** (height - 1)


def right_child(i, height):
    return i + 2 ** (height - 1)


def is_valid_tree(binary_number, node, height):
    if height <= 0:
        return True

    left_node = left_child(node, height)
    right_node = right_child(node, height)

    left = is_valid_tree(binary_number, left_node, height - 1)
    right = is_valid_tree(binary_number, right_node, height - 1)

    if not left or not right:
        return False

    if binary_number[node] == "0":
        if binary_number[left_node] == "1":
            return False
        if binary_number[right_node] == "1":
            return False

    return True


def solution(numbers):
    answer = []
    for number in numbers:
        binary_number = bin(number)[2:]
        binary_length = len(binary_number)

        for i in range(1, 7):
            if (2 ** i - 1) < binary_length:
                continue
            else:
                zerofill = binary_number.zfill(2 ** i - 1)
                if is_valid_tree(zerofill, len(zerofill) // 2, i - 1):
                    answer.append(1)
                    break
        else:
            answer.append(0)

    return answer
