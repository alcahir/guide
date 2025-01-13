from typing import List


def task_1(array: List[int], target: int) -> List[int]:
    hashmap = set()
    for idx in range(len(array)):
        if target - array[idx] in hashmap:
            return [target - array[idx], array[idx]]
        hashmap.add(array[idx])
    return []


def task_2(number: int) -> int:
    newnum = 0
    input_num = abs(number)
    while input_num > 0:
        newnum = newnum * 10 + input_num % 10
        input_num = input_num // 10
    if number < 0:
        return 0 if -newnum < -(2 ** 31) - 1 else -newnum

    return newnum if newnum < 2 ** 31 else 0


def task_3(array: List[int]) -> int:
    ans = -1
    n = len(array)

    for idx in range(n):
        num = abs(array[idx])

        if array[num - 1] < 0:
            ans = num
            break

        array[num - 1] *= -1

    return ans


def task_4(string: str) -> int:
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    ans = symbols[string[-1]]
    for i in range(len(string) - 2, -1, -1):
        if symbols[string[i]] < symbols[string[i + 1]]:
            ans -= symbols[string[i]]
        else:
            ans += symbols[string[i]]
    return ans


def task_5(array: List[int]) -> int:
    min_val = float("inf")

    for num in array:
        if num < min_val:
            min_val = num
    return min_val
