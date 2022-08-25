import task1_3
import task4_5


print("task 1")
task1_3.find_most_frequently_repeated_words('Hi! How are are you you? Hi! I am okay')
print("*"*20)

print("task 2")
task1_3.sort_grades(['b', 'c', 'C', 'f', 'A', 'z'])
print("*" * 20)

print("task 3")
task1_3.is_anagram('car', 'tar')  # False
task1_3.is_anagram('car', 'cart')  # False
task1_3.is_anagram('anagram', 'nagaram')  # True
task1_3.is_anagram('beluga', 'begula')  # True
print("*" * 20)

print("task 4")
task4_5.sort_array([3, 1])  # [1, 3]
task4_5.sort_array([3, 2, -1, 4])  # [-1, 2, 3, 4]
task4_5.sort_array([5, 3, 2, 8, 1, 4])  # [1, 3, 2, 8, 5, 4]
print("*" * 20)

print("task 5")
task4_5.roman_to_int('XXI')  # 21
task4_5.roman_to_int('IV')  # 4
task4_5.roman_to_int('I')  # 1
print("*" * 20)
