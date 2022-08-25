import re
from collections import Counter
from decorators import print_result


# Задание №1
#
# Условие:
# Написать функцию, которая находит самые повторяющиеся слова в строке.
#
# Пример:
#
# simple_text('Am I want write code? Yeah! I like it') → I
# simple_text('Hi! How are you? Hi! I am okay') → Hi
# simple_text('test text test and test that again') → test
@print_result
def find_most_frequently_repeated_words(text: str):
    words = re.findall(r'\w+', text)
    # upper возможно лишний, но решил что это подходит больше для логики функции
    cap_words = [word.upper() for word in words]
    word_counts = Counter(cap_words)
    max_value = max(word_counts.values())
    list_result = []
    for key, value in word_counts.items():
        if value == max_value:
            list_result.append(key)

    return f'{", ".join(list_result)} \nКоличество повторений слов выше: {max_value}'


# Задание №2
#
# Условие:
#
# Написать функцию, которая сортирует список с оценками на основе английской системы.
# Всего 5 символов, в порядке убывания: A, B, C, D, F.
#
# Примеры:
#
# sort_grades(['A', 'B', 'C', 'C', 'F', 'A']) -> ['F', 'C', 'C', 'B', 'A', 'A']
# sort_grades(['b', 'c', 'C', 'f', 'A']) -> ['F', 'C', 'C', 'B', 'A']
# sort_grades([]) -> []
@print_result
def sort_grades(grades: list):
    permitted_grades = ("A", "B", "C", "D", "F")
    final_list = list()
    for item in grades:
        upper_item = item.upper()
        if upper_item not in permitted_grades:
            print(f"Неопознанная отметка: {upper_item}. Символ пропущен.")
        else:
            final_list.append(upper_item)
    return sorted(final_list, reverse=True)


# Задание №3
#
# Условие:
#
# Написать функцию, которая проверяет, являются ли две строки анаграммами?
# На вход идут две строки, состоящие из символов английского алфавита.
#
# Примеры:
#
# is_anagram('car', 'tar') -> False
# is_anagram('car', 'cart') -> False
# is_anagram('anagram', 'nagaram') -> True
# is_anagram('beluga', 'begula') -> True
@print_result
def is_anagram(word_1, word_2):
    return sorted(word_1) == sorted(word_2)
