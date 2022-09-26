#Задание 1 Напишите программу, которая принимает на вход
#вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11
#a = int(input('Введите одно число: '))
#sum = 0
#while a > 0:
#    num = a % 10
#    sum += num
#    a = a // 10
#print('Сумма цифр введенного Вами числа: ', sum)


#Задание 2 Напишите программу, которая принимает на вход число
#N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#N = int(input('Введите число N: '))
#for i in range(N):
#result = (-3)**i 
#print(result, end=" ")

#N = int(input('Введите число N: '))
#factorial = 1
#for i in range(1, N+1):
#     factorial *= i
#     print(factorial, end=' ')

#Задание 3 Задайте список из n чисел последовательности
#(1+1/n)^n и выведите на экран их сумму,округлённую до трёх знаков после точки.
#Пример:
# def float_range(N):
#     list = []
#     for i in range(1, N):
#         list.append(float((1 + 1/i)**i))
#     return list

# N = int(input('Введите число: '))
# list = float_range(N)
# print ('Сумма, округленная до третьего знака: ', round(sum(list), 3))

#Задание 4 Задайте список из N элементов, заполненных числами из
#промежутка [-N, N]. Найдите произведение элементов на
#позициях a и b. Значения N, a и b вводит пользователь с клавиатуры.
#from re import A
# N = int(input("Введите размер списка: "))
# spam = list(range(-N, N+1))
# print(spam)
# print ('Обратите внимание, что позиции списка начинаются с 0')
# A = int(input('Введите позицию первого множителя: '))
# B = int(input('Введите позицию второго множителя: '))
# if B <=-1 or A <=-1 or B >=N or A >=N:
#     print('Введите значение от 0 до N')
# else:
#     s= (spam[A]*spam[B])
#     print ('Ответ:',s)

#Задание 5 Реализуйте алгоритм перемешивания списка.
#Не используя стандартную функцию
# import random

# def my_shuffle(lst):
#     for i in range(len(lst)):
#         rand = random.randrange(0, len(lst))
#         tmp = lst[i]
#         lst[i] = lst[rand]
#         lst[rand] = tmp
    
# print ("Изначально:")
# lst = ["Хрю", "ши", "не", "бу", "дет", ",", "он", "в", "котле"]
# print(lst)
# print("Перемешано:")
# my_shuffle(lst)
# print(lst)

#Задание 6 Напишите программу, в которой пользователь будет
#задавать две строки, а программа - определять количество
#вхождений одной строки в другой.
#Пример
#-Для "abababb" и "aba" -> 2
# def substr_count(string, substring):
#     cnt = 0
#     occur = -1
#     while True:
#         occur = string.find(substring, occur + 1)
#         if occur == -1:
#             return cnt
#         cnt += 1

# string = "abababb"
# substring = "aba"
# cnt = substr_count(string, substring)
# print("Вхождений:", cnt)