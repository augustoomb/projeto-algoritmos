# Baseado em: https://stackoverflow.com/questions/48017422
# /implementing-quick-sort-in-python

def quick_sort(arr):
    tam_arr = len(arr)
    if tam_arr <= 1:
        return arr
    meio_do_arr = tam_arr // 2
    pivot = arr[meio_do_arr]
    esq = [x for x in arr if x < pivot]
    dir = [x for x in arr if x > pivot]
    meio = [x for x in arr if x == pivot]
    return quick_sort(esq) + meio + quick_sort(dir)


def check_if_positive_number(arr):
    return all((isinstance(n, int) and n > 0) for n in arr)


def find_duplicate(nums):
    if check_if_positive_number(nums) is False:
        return False

    sorted_list = quick_sort(nums)

    repeated_number = False

    for index in range(len(sorted_list) - 1):
        if sorted_list[index] == sorted_list[index + 1]:
            repeated_number = sorted_list[index]

    return repeated_number

# nums = [1, 3, 4, 2, -2]
# print(find_duplicate(''))
# print(check_if_positive_number(nums))
