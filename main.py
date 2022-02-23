# 1 Найти самую длинную подстроку без повторений в строке;
#
# "aba" -> "ab" или "ba", 2
# "aaaaa" -> "a", 1
# "abcde" -> "abcde", 5
# "" -> "", 0
#
#
# 2 Найти в строке самый длинный палиндром
# "" -> ""
# "aa" -> "aa"
# "aaa" -> "aaa"
# "aba" -> "aba"
# "abba" -> "abba"
# "abbasfdjkfhlgfgfgfgfg" -> "gfgfgfgfg"
# "abbasfdjkfhlgfgfgfgfgaba" -> "gfgfgfgfg"
# "abbasfdjkfhlgfgfgfgfgabasadfsa" -> "gfgfgfgfg"
#
# Проверить скорость работы на строке длиной 1000 символов (в которой есть несколько полиндромов произвольной длины в разных частях строки). Код для генерации такой строки приложить
#
# 3 Остановить вложенный цикл
#
# использовать для этого break и continue
#
# 4 На вход подается строка. Необходимо посчитать количество каждых символов и вывести в виде словаря. "abababa" {'a': 4, 'b': 3}
#
# 5 Решить задачу подсчета элементов в словаре с использованием try ... except
#
# 6 Сравнить по скорости 4 метода решения задачи подсчета символов в строке
#
# 1. try ... except
# 2. collections.Counter
# 3. dict.get
# 4. if el in dict.keys() ... else ...


# 7 Реализовать класс Калькулятор, у которого будут методы sum, multiple, причем необходимо обеспечить возможность вызова методов по цепочке.

# c = Calculator(10);
# c.sum(8).sum(6).sum(5).multiple(2); print(c) -> 58

# 8 С помощью pip установить пакет в локальную директорию
# Что посмотреть: PEP-8, Укус Питона, freecodecamp, stepik

# 9 Написать свою реализацию функции sorted

# 10 Необходимо реализовать функцию для сортировки элементов списка. Должен работать функционал по передаче аргумента key внутрь функции.


# 1 Найти самую длинную подстроку без повторений в строке;
#
# "aba" -> "ab" или "ba", 2
# "aaaaa" -> "a", 1
# "abcde" -> "abcde", 5
# "" -> "", 0

# def max_substr(str):
#     ma = ''
#     while len(str) > 0:
#         cur_str = ''
#         for i in str:
#             if i in cur_str:
#                 if len(ma) < len(cur_str):
#                     ma = cur_str
#                 break
#             else:
#                 cur_str += i
#         ma = max(ma, cur_str, key=len)
#         str = str[1:]
#     return ma
#
#
# str = "aba"
# print(max_substr(str), len(max_substr(str)))
# str = "aaaaa"
# print(max_substr(str), len(max_substr(str)))
# str = "abcde"
# print(max_substr(str), len(max_substr(str)))
# str = ""
# print(max_substr(str), len(max_substr(str)))
# str = "abbasfdjkfhlgfgfgfgfg"
# print(max_substr(str), len(max_substr(str)))

# 2 Найти в строке самый длинный палиндром
# "" -> ""
# "aa" -> "aa"
# "aaa" -> "aaa"
# "aba" -> "aba"
# "abba" -> "abba"
# "abbasfdjkfhlgfgfgfgfg" -> "gfgfgfgfg"
# "abbasfdjkfhlgfgfgfgfgaba" -> "gfgfgfgfg"
# "abbasfdjkfhlgfgfgfgfgabasadfsa" -> "gfgfgfgfg"

# def palindrome(str):
#     n = len(str)
#     array_substr = list()
#     for i in range(n):
#         for j in range(i, n):
#             new_str = ''
#             for z in range(i, j + 1):
#                 new_str += str[z]
#             array_substr.append(new_str)
#     ma = -1
#     pal = ''
#     for i in array_substr:
#         if i == i[::-1]:
#             if len(i) > ma and len(i) > 1:
#                 ma = len(i)
#                 pal = i
#     return pal
#
#
# print(palindrome(''))
# print(palindrome('aa'))
# print(palindrome('aaa'))
# print(palindrome('aba'))
# print(palindrome('abba'))
# print(palindrome('abbasfdjkfhlgfgfgfgfg'))
# print(palindrome('abbasfdjkfhlgfgfgfgfgaba'))
# print(palindrome('abbasfdjkfhlgfgfgfgfgabasadfsa'))
#
# import random
# import string
#
#
# def generate_random_string(length):
#     letters = string.ascii_lowercase
#     rand_string = ''.join(random.choice(letters) for i in range(length))
#     return rand_string
#
# from datetime import datetime
# start_time = datetime.now()
# str = generate_random_string(1000)
# print(palindrome(str), datetime.now() - start_time)


# 3 Остановить вложенный цикл
# a = [1, 2, 3]
# b = [10, 20, 30, 40]
# for i in a:
#     for j in b:
#         if j == 30:
#             break
#         print(i, j)
# print('-------------')
# a = [1, 2, 3]
# b = [10, 20, 30, 40]
# for i in a:
#     for j in b:
#         if j >= 30:
#             continue
#         else:
#             print(i, j)


# 4 На вход подается строка. Необходимо посчитать количество каждых символов и вывести в виде словаря. "abababa" {'a': 4, 'b': 3}
# 5 Решить задачу подсчета элементов в словаре с использованием try ... except
# 6 Сравнить по скорости 4 метода решения задачи подсчета символов в строке
# 1. try ... except
# 2. collections.Counter
# 3. dict.get
# 4. if el in dict.keys() ... else ...

# class task():
#     def __init__(self, str):
#         self.str = str
#
#     def try_except(self):
#         start_time = datetime.now()
#         count_dict = dict()
#         str = self.str
#         for el in str:
#             if el == ' ':
#                 continue
#             try:
#                 count_dict[el] += 1
#             except KeyError:
#                 count_dict[el] = 1
#         print('try_except', count_dict, datetime.now() - start_time)
#
#     def collections_counter(self):
#         from collections import Counter
#         start_time = datetime.now()
#         str = self.str
#         print('collections.Counter', Counter(str), datetime.now() - start_time)
#
#     def get(self):
#         start_time = datetime.now()
#         str = self.str
#         count_dict = dict()
#         for el in str:
#             if el == ' ':
#                 continue
#             if count_dict.get(el, False):
#                 count_dict[el] += 1
#             else:
#                 count_dict[el] = 1
#         print('get', count_dict, datetime.now() - start_time)
#
#     def keys(self):
#         start_time = datetime.now()
#         str = self.str
#         count_dict = dict()
#         for el in str:
#             if el == ' ':
#                 continue
#             if el in count_dict.keys():
#                 count_dict[el] += 1
#             else:
#                 count_dict[el] = 1
#         print('keys', count_dict, datetime.now() - start_time)
#
#     def generator(self):
#         start_time = datetime.now()
#         str = self.str
#         print('generator', {k: str.count(k) for k in set(str) if k not in " "}, datetime.now() - start_time)
#
#     def simple_cycle(self):
#         start_time = datetime.now()
#         str = self.str
#         count_dict = dict()
#         for el in str:
#             if el == " ":
#                 continue
#             count_dict[el] = str.count(el)
#         print('simple cycle', count_dict, datetime.now() - start_time)
#
#
# from datetime import datetime
#
# a = task("caaab cd")
# a.try_except()
# a.collections_counter()
# a.get()
# a.keys()
# a.generator()
# a.simple_cycle()


# 7 Реализовать класс Калькулятор, у которого будут методы sum, multiple, причем необходимо обеспечить возможность вызова методов по цепочке.
# c = Calculator(10); c.sum(8).sum(6).sum(5).multiple(2); print(c) -> 58

# class Calculator:
#     def __init__(self, value):
#         self.value = value
#
#     def sum(self, value):
#         self.value += value
#         return self
#
#     def multiple(self, value):
#         self.value *= value
#         return self.value
#
#
# c = Calculator(10)
# print(c.sum(8).sum(6).sum(5).multiple(2))

# 9 Написать свою реализацию функции sorted
# 10 Необходимо реализовать функцию для сортировки элементов списка. Должен работать функционал по передаче аргумента key внутрь функции.

# def sort_array(array):
#     length_of_array = len(array)
#     for i in range(length_of_array):
#         for j in range(length_of_array):
#             if array[i] < array[j]:
#                 array[i], array[j] = array[j], array[i]
#     print(array)


# a = [1, 3, 4, 2, 10]
# s = sort_array(a)
