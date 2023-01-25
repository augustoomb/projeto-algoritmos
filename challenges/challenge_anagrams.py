# remover acentos
from unidecode import unidecode


def is_anagram(first_string, second_string):
    arr_primeira_str_ordenada = quick_sort(
        list(unidecode(first_string).lower())
    )
    arr_segunda_str_ordenada = quick_sort(
        list(unidecode(second_string).lower())
    )
    primeira_str = ''.join(arr_primeira_str_ordenada)
    segunda_str = ''.join(arr_segunda_str_ordenada)
    comparacao = primeira_str == segunda_str
    return (primeira_str, segunda_str, comparacao)


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


# print(is_anagram("Augusto", "OtsuguA"))
