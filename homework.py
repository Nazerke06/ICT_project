# def find_numbers():
#     a = []
#
#     for number in range(1500, 2701):
#         if number > 7 and number % 5 == 0:
#             a.append(number)
#
#     return a
# numbers_list = find_numbers()
# print(numbers_list)
# task2
# print("Цельсийді фаренгейтке айналдыру үшін енгізіңіз:" )
# c=int(input())
# e=((c//5)*9)+32
# print(e)
# print("Цельсийді айналдыру үшін енгізіңіз:")
# f=int(input())
# v=5*((f-32)//9)
# print(v)
# task 3
# import random
# a=random.randint(1, 9)
# while True:
#     i=int(input("1-ден 9-ға дейінгі санды табыңыз: "))
#     if a == i :
#         print("жақсы болжады!")
#         break
#     else:
#         print("Қате болжам,қайта жаз")
# task 4
# def create_pattern(rows):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print("*", end=" ")
#         print()
#
#     for i in range(rows - 1, 0, -1):
#         for j in range(1, i + 1):
#             print("*", end=" ")
#         print()
# num_rows = int(input())
# create_pattern(num_rows)
# task 5
# def fibonacci_series(n):
#     fib_series = [0, 1]
#     while fib_series[-1] + fib_series[-2] <= n:
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series[1:]
# limit = int(input())
# result = fibonacci_series(limit)
# print(limit, ":", " ".join(map(str, result)))
# task 6
# numbers = []
# total_sum = 0
# count = 0
# while True:
#     try:
#         num = int(input())
#         if num == 0:
#             break
#         total_sum += num
#         count += 1
#     except ValueError:
#         print("Қате енгізу, қайта енгізіңіз")
# if count > 0:
#     average = total_sum / count
#     print(total_sum)
#     print(average)
# else:
#     print("Сан енгізілген жоқ")
#
# task 7
# a= int(input())
# for i in range(1, a + 1):
#     print(str(i) * i, " ")
# task 9
# while True:
#     string = input()
#     if string == "":
#         break
#     print(string.lower())
# task 10
# a= int(input())
# b= int(input())
# c=int(input())
# m=1/2*math.sqrt((2*a**2)+(2*b**2)+(2*c**2))
# print(m)
# a= int(input())
# b= int(input())
# c=int(input())
# if a<b<c:
#     print(b)
# elif c<b<a:
#     print(b)
# elif a<c<b:
#     print(c)
# elif b<c<a:
#     print(c)
# elif b<a<c:
#     print(a)
# else:
#     print(a)