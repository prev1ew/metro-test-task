from decorators import print_result


# для таски номер 5
CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


# Задание №4
#
# Условие:
#
# Написать функцию, которая сортирует список, но все четные числа должны остаться на своем месте.
#
# Примеры:
#
# sort_array([3, 1]) -> [1, 3]
# sort_array([3, 2, -1, 4]) -> [-1, 2, 3, 4]
# sort_array([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]
@print_result
def sort_array(array):
    dict_even = dict()
    list_not_even = list()
    for pos, item in enumerate(array):
        if item % 2:
            list_not_even.append(item)
        else:
            dict_even[pos] = item

    list_not_even.sort()

    final_list = []
    i = 0
    while i < len(array):
        if i in dict_even.keys():
            final_list.append(dict_even.pop(i))
        else:
            final_list.append(list_not_even.pop(0))
        i += 1
    return final_list


# Задание №5
#
# Условие:
#
# Написать функцию которая, будет переводить римские символы в привычную нам десятичную систему.
#
# Пример:
#
# roman_to_int('XXI') -> 21
# roman_to_int('IV') -> 4
# roman_to_int('I') -> 1
@print_result
def roman_to_int(txt):
    # тут можно было использовать библиотеку roman, но решил так
    txt = txt.upper()
    result = 0
    for int_val, roman_val in CONV_TABLE:
        while txt.startswith(roman_val):
            result += int_val
            txt = txt[len(roman_val):]
    return result
