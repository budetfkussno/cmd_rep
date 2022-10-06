# Задача 1
# Вычислить число π c заданной точностью d


#  Задача 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите натуральное число: '))
# lst = [n]

# def natur(lst):
#     fl = 0
#     for i in range(lst[-1] // 2, 1, -1):
#         if lst[len(lst)-1] % i == 0:
#             lst.append(i)
#             lst[-2] = lst[-2] // i              
#             fl += 1
#     if fl != 0:
#         natur(lst)

# natur(lst)
# print(lst)

#  Задача 3
#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# lst = list(map(int, input('Введите числа через пробел:\n').split()))
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f'Список оставшихся элементов: {new_lst}')

#  Задача 4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# def mnogochlen(k):
#     mnogochlen = "k = " + str(k) + " => "
#     for i in range(k, -1, -1):
#         # Так будет много отсутствуюших членов
#         number = random.randrange(0, 4)
#         if number != 0 or i == k: # Второе условие если нам всгеда нужен первый член
#             number = random.randrange(1, 101)
#         # Так будет мало отсутсвующих членов
#         # number = random.randrange(0, 101)
#         if number != 0 and i != 0:
#             if random.randrange(0,4) == 0:
#                 curr_chlen = str(number) + "x^" + str(i) + " - "
#             else:
#                 curr_chlen = str(number) + "x^" + str(i) + " + "
#             mnogochlen += curr_chlen
#         elif number != 0 and i == 0:
#             mnogochlen += str(number)
#         elif number == 0 and i == 0:
#             mnogochlen = mnogochlen[:-3]
#     mnogochlen += " = 0"
#     f = open('mnogochlen.txt', 'w')
#     f.write(mnogochlen + '\n')
#     f.close()
#     return mnogochlen

# k = -1
# while k < 0 or k > 100:
#     k = int(input("Введите коэффициент: "))
#     if k < 0 or k > 100:
#         print ("Ошибка, введите снова!")
# print(mnogochlen(k))

# # Задача 5
# # Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# def mnogochlen_sum():
#     file1 = open ('file1.txt', 'r')
#     file2 = open ('file2.txt', 'r')
#     file3 = open ('file3.txt', 'w')
#     last1 = 0
#     last2 = 0
#     mnogochlen1 = file1.read()
#     file1.close()
#     mnogochlen2 = file2.read()
#     file2.close()
#     lst1, last1 = get_list(mnogochlen1)
#     lst2, last2 = get_list(mnogochlen2)
#     result = []
#     k1 = lst1[0][lst1[0].find("^") + 1:]
#     k2 = lst2[0][lst2[0].find("^") + 1:]
#     print(lst1)
#     print(lst2)
#     if k1 >= k2:
#         result = get_sum(lst1, lst2)
#     else:
#         result = get_sum(lst2, lst1)
#     if last1 + last2 != 0:
#         result.append(str(last1 + last2))
#     print("Многочлен 1:")
#     print(mnogochlen1)
#     print("Многочлен 2:")
#     print(mnogochlen2)
#     print("Сумма многочленов:")
#     print(result)
#     file3.write(get_str_from_list(result) + '\n')
#     file3.close()
        
# def get_list(mnogochlen):
#     lst = []
#     last = 0
#     mnogochlen = mnogochlen.replace(' ', '')
#     chlen = ""
#     for i in range(len(mnogochlen)):
#         if mnogochlen[i] != '+' and mnogochlen[i] != '-' or mnogochlen[i] == '-' and i == 0:
#             chlen += mnogochlen[i]
#         else:
#             lst.append(chlen)
#             if mnogochlen[i] == '-':
#                 chlen = mnogochlen[i]
#             else:
#                 chlen = ""
#     v1 = mnogochlen.find("=")
#     v2 = mnogochlen.rfind("+")
#     v3 = mnogochlen.rfind("-")
#     if v2 > v3:
#         if "^" not in mnogochlen[v2:v1]:
#             last = int(mnogochlen[v2:v1])
#         else:
#             lst.append(mnogochlen[v2:v1]) 
#     else:
#         if "^" not in mnogochlen[v3:v1]:
#             last = int(mnogochlen[v3:v1])
#         else:
#             lst.append(mnogochlen[v3:v1])
#     return lst, last

# def get_sum(lst1, lst2):
#     result = []
#     for i in range(len(lst1)):
#         chlen = find_coeff(lst1[i], lst2)
#         if chlen not in result:
#             if chlen[0:3] != "0x^":
#                 result.append(chlen)
#     for i in range(len(lst2)):
#         k2 = int(lst2[i][lst2[i].find("^") + 1:])
#         for j in range(len(result)):
#             k1 = int(result[j][result[j].find("^") + 1:])
#             if k2 > k1:
#                 result.insert(j, lst2[i])
#                 break
#             elif k2 == 1:
#                 result.append(lst2[i])
#                 break
#     return result 

# def find_coeff(chlen1, lst):
#     for i in range(len(lst)):
#         chlen2 = lst[i]
#         k1 = int(chlen1[chlen1.find("^") + 1:])
#         k2 = int(chlen2[chlen2.find("^") + 1:])     
#         if k1 == k2:
#             v1 = int(chlen1[0:chlen1.find("x")])
#             v2 = int(chlen2[0:chlen2.find("x")])
#             lst.pop(i)
#             return str(v1 + v2) + "x^" + str(k1)
#     return chlen1

# def get_str_from_list(lst):
#     result = ""
#     for i in range(len(lst)):
#         if i != len(lst) - 1:
#             if i + 1 <= len(lst) - 1:
#                 if "-" in str(lst[i + 1]):
#                     lst[i + 1] =  lst[i + 1].replace('-', '')
#                     result += str(lst[i]) + " - "
#                 else:
#                     result += str(lst[i]) + " + "
#         elif i == len(lst) - 1:
#             result += str(lst[i]) + " = 0"
#     return result

# mnogochlen_sum()