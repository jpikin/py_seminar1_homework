# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# num = int(input())
# print(num // 100 + num % 100 // 10 + num % 10)

#############################################################


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# while (True):
#     s = int(input("Введите число кратное 6 -> "))
#     if S % 6 == 0: break
#     else: print("Число не кратно 6 :-(")

# p = int(s/6)
# k = p*4
# print(p, k, p)

##############################################################


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:
# 385916 -> yes
# 123456 -> no

# def sum(num):
#     return num // 100 + num % 100 // 10 + num % 10

# tiket = input("Введите номер билета ")
# first_half = sum(int(tiket[:3]))
# second_half = sum(int(tiket[3:]))

# print("yes" if first_half == second_half else "no")

################################################################


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

# h_chocolate = int(input("высота шоколадки..."))
# w_chocolate = int(input("ширина шоколадки..."))

# while (True):
#     piece = int(input("Введите необходимое количество долек "))
#     if piece <= h_chocolate * w_chocolate: break
#     else: print("Шоколадка не на столько большая...")


# if piece == 1:
#     if h_chocolate == 1 or w_chocolate == 1: print('yes')
#     else: print('no')
# else:
#     if piece % 2 == 0:
#         if w_chocolate % 2 == 0 or h_chocolate % 2 == 0: print('yes')
#         else: print('no')
#     else:
#         if w_chocolate % 2 != 0 or h_chocolate % 2 != 0: print('yes')
#         else: print('no')     

#### 2 Вариант решения 8 задачи:

# if piece % h_chocolate == 0 or piece % w_chocolate == 0: print('yes')
# else: print('no')

