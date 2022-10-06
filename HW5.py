# Задача 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# with open('file_words.txt', 'w') as data:
#     data.write('Текст текабвст, из которого которогоабв надо удаабвлить удалить')
# with open('file_words.txt', 'r') as data:
#     string = data.readline()

# def del_words(fined_text):
#     fined_text = list(filter(lambda x: 'абв' not in x, fined_text.split()))
#     return " ".join(fined_text)

# with open('file_words.txt', 'r') as file:
#     fined_text = file.read()

# with open('file_words_2.txt', 'w') as file:
#     fined_text = del_words(fined_text)
#     file.write(fined_text)

# print('Осталось: ' + fined_text)

# Задача 2
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.
# b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, то он, однозначно, проиграет.
# Достаточно довести игру до такой ситуации.

# from random import *
# import os


# welcome_text = ('Приветствую Вас, хотите сыграть в игру?\n'
#                 'Для начала я расскажу правила:\n'
#                 'Я даю Вам 2021 конфету, вы берете их поочереди,\n'
#                 'причем, за один раз можно взять не больше 28 конфет.\n'
#                 'Выигрывает тот, кто последним ходом заберет все конфеты.\n')
# print(welcome_text)

# message = ['твоя очередь', 'бери уже', 'бери больше', 'бери быстрее']


# def player_vs_player():
#     candies_total = 2021
#     max_take = 28
#     count = 0
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = input('\nА твоего соперника?: ')

#     print(f'\nНу чтож {player_1} и  {player_2} игра начинается!\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     x = randint(1, 2)
#     if x == 1:
#         lucky = player_1
#         loser = player_2
#     else:
#         lucky = player_2
#         loser = player_1
#     print(f'Поздравляю {lucky} ты ходишь первым !')

#     while candies_total > 0:
#         if count == 0:
#             step = int(input(f'\n{choice(message)} {lucky} = '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nНе жадничай {lucky} можно взять только {max_take} конфет, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 1
#         else:
#             print('Все кончились конфетки')

#         if count == 1:
#             step = int(input(f'\n{choice(message)}, {loser} '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nНе жадничай {loser} можно взять только {max_take} конфет, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 0
#         else:
#             print('Кончились конфеты')

#     if count == 1:
#         print(f'{loser} ПОБЕДИЛ')
#     if count == 0:
#         print(f'{lucky} ПОБЕДИЛ')


# player_vs_player()


# def player_vs_bot():
#     candies_total = 2021
#     max_take = 28
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = 'Компьютер'
#     players = [player_1, player_2]
#     print(f'\nНу чтож {player_1} и  {player_2} игра начинается!\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     lucky = randint(-1, 0)

#     print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step

#     print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()

# Задача 3
# Создайте программу для игры в ""Крестики-нолики"".
# Пример интерфейса:

#    |   | 0
# -----------    
#    |   |
# -----------
#    | X |

# X="X"
# O="O"
# EMPTY=' '
# TIE="Ничья"
# NUM_SQUARES=9

# def display_instruct():
#     '''Выводит на экран  иснтрукцию для игрока'''
#     print(
# """
# Что бы сделать свой ход , введите от 0 до 8.
# Числа соответсвуют полям доски:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8
# Приготовься к игре! \n
# """
#         )
# def ask_yes_no(question):
#     """Задает вопросы с ответом 'Да' или'Нет".    """
#     response=None
#     while response not in("y","n"):
#         response=input(question).lower()
#     return response
# def ask_number(question, low, high):
#     """Просит ввести число из диапазона."""
#     response=None
#     while response not in range(low,high):
#         response=int(input(question))
#     return response
# def pieces():
#     "Определяет принадлежность первого хода"
#     go_first=ask_yes_no("Хочешь ходить первым?(y/n): ")
#     if go_first=="y":
#         print ("\n Ну что ж, играй крестиками")
#         human = X
#         computer = O
#     else:
#         print("\n Спасибо, что предоставил право перового хода компьютеру")
#         computer = X
#         human = O
#     return computer, human
# def new_board():
#     "Создает новую игровую доску"
#     board = []
#     for square in range(NUM_SQUARES):
#         board.append(EMPTY)
#     return board
# def  display_board(board):
#     """Отображает  игровую  доску  на  экране."""
#     print("\n\t", board[0], "|", board[1],"|",board[2])
#     print("\t",  "---------")
#     print("\n\t", board[3], "|", board[4],  "|", board[5])
#     print("\t",  "---------")
#     print("\n\t", board[6], "|", board[7],  "|",  board[8],"\n")

# def legal_moves(board):
#     """Создает список доступных ходов """
#     moves=[]
#     for square in range(NUM_SQUARES):
#         if board[square] == EMPTY:
#             moves.append(square)
#     return moves
# def winner(board):
#     """Определяет победителя в игре """
#     WAYS_TO_WIN=((0,1,2),
#                  (3,4,5),
#                  (6,7,8),
#                  (0,3,6),
#                  (1,4,7),
#                  (2,5,8),
#                  (0,4,8),
#                  (2,4,6))
#     for row in WAYS_TO_WIN:
#         if board[row[0]]==board[row[1]]==board[row[2]] !=EMPTY:
#             winner=board[row[0]]
#             return winner
#         if EMPTY not in board:
#             return TIE
#     return None

# def human_move(board,human):
#     """ Получает ход человека"""
#     legal=legal_moves(board)
#     move=None
#     while move not in legal:
#         move=ask_number("Твой ход. Выбери одно из полей (0-8):",0, NUM_SQUARES)
#         if move not in legal:
#             print ("\nЭто поле уже занято. Выбери другое.\n")
#     print("Хорошо.....")
#     return move
# def computer_move(board, computer, human):
#     """Делает ход копмьютер """
#     board=board[:]
#     BEST_MOVES=[4,0,2,6,8,1,3,5,7]
#     print("Я выберу номер", end=" ")
#     for move in legal_moves(board):
#         board[move]=computer
#         if winner(board)==computer:
#             print(move)
#             return move
#         board[move]=EMPTY
#     for move in BEST_MOVES:
#         if move in legal_moves(board):
#             print(move)
#             return move
# def next_turn(turn):
#     """Осуществляет  переход хода."""
#     if turn==X:
#         return O
#     else:
#         return X
# def congrat_winner(the_winner, computer, human):
#     """Поздравляем;  победителя  игры."""
#     if the_winner !=TIE:
#         print("Три",the_winner,"в ряд!\n")
#     else:
#         print("Ничья!\n")
#     if the_winner == computer:
#         print("Победил кмопьютер!")
#     elif the_winner==human:
#         print("Поздравляю,Вы победили компьютер!")
#     elif the_winner==TIE:
#         print("Ничья!")
# def main():
#     """Основная часть программы """
#     display_instruct()
#     computer, human =pieces()
#     turn = X
#     board = new_board()
#     display_board(board)
#     while not winner(board):
#         if turn ==human:
#             move=human_move(board,human)
#             board[move]=human
#         else:
#             move=computer_move(board,computer,human)
#             board[move]=computer
#         display_board(board)
#         turn = next_turn(turn)
#     the_winner=winner(board)
#     congrat_winner(the_winner,computer,human)

# main()
# input("\n\nНажмите Enter, чтобы выйти.")


# Задача 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('file_5_1.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

# with open('file_5_1.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_5_1.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_5_2.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Входные данные: \t' + decoded_string)
# print('Выходные данные: \t' + rle_encode(decoded_string))
# print(f'Коэффициент сжатия: \t{round(len(decoded_string) / len(encoded_string), 1)}')