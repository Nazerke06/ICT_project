# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)
# a = True
# b = False
# print(a and b or not a and not b)
# A=int(input())
# B=int(input())
# H=int(input())
# if A<H and H<B:
#     print("Это нормально")
# elif A>H:
#     print("Недосып")
# else:
#     print("Пересып")
# a=int(input())
# if a%4==0 and a%100!=0:
#     if a%400==0:
#         print("Високосный")
# else:
#     print("Обычный")
# print("123" + "42")
import math
import random

# a=float(input())
# b=float(input())
# c=float(input())
# def calculate_triangle_area(a, b, c):
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     return area
# triangle_area = calculate_triangle_area(a, b, c)
# print(triangle_area)
# a=int(input())
# if (a>-15 and a<=12) or (14<a<17) or(19<=a):
#     print(True)
# else:
#     print(False)
# a=int(input())
# b=int(input())
# c=int(input())
# d="треугольник"
# f="прямоугольник"
# k="круг"
# def calculate_triangle_area(a, b, c):
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     return area
# triangle_area = calculate_triangle_area(a, b, c)
# print(triangle_area,d)

# def calculate_room_area(shape, *args):
#     if shape == "triangle":
#         if len(args) == 2:
#             base, height = args
#             area = 0.5 * base * height
#         else:
#             print("Invalid number of parameters for a triangle.")
#             return None
#     elif shape == "rectangle":
#         if len(args) == 2:
#             length, width = args
#             area = length * width
#         else:
#             print("Invalid number of parameters for a rectangle.")
#             return None
#     elif shape == "circle":
#         if len(args) == 1:
#             radius = args[0]
#             area = math.pi * radius**2
#         else:
#             print("Invalid number of parameters for a circle.")
#             return None
#     else:
#         print("Invalid room shape.")
#         return None
#
#     return area
# a=int(input())
# b=int(input())
# c=int(input())
# if (a>b and a>c) and (b>c):
#     print(a)
#     print(c)
#     print(b)
# elif (b>a and b>c) and a>c:
#     print(b)
#     print(c)
#     print(a)
# elif (c>a and c>b) and a>b:
#     print(c)
#     print(b)
#     print(a)
# elif (c>a and c>b) and b>a:
#     print(c)
#     print(a)
#     print(b)
# elif (a>=b and a>c) and (b>c):
#     print(a)
#     print(c)
#     print(b)
# elif (c>=a and c>b) and a>b:
#     print(a)
#     print(b)
#     print(c)
# elif (c>=a and c>b) and b>a:
#     print(b)
#     print(a)
#     print(c)
# elif (b>=a and b>=c) and a>=c:
#     print(a)
#     print(b)
#     print(c)
# elif (a==c and a<b) and c<b:
#     print(b)
#     print(a)
#     print(c)
# elif (b==c and a>b) and a>c:
#     print(a)
#     print(b)
#     print(c)
# def calculate_sum_of_numbers():
#     total_sum = 0
#
#     while True:
#         try:
#             num = int(input())
#         except ValueError:
#             print()
#             continue
#
#         if num == 0:
#             break
#         else:
#             total_sum += num
#
#     return total_sum
#
# result = calculate_sum_of_numbers()
# print(result)
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
#     print(i)
# print('I', 'Like','Python', sep='***')
# print('Mars', 'Jupiter', sep='**', end='?')
# a=int(input())
# b=int(input())
# c=int(input())
# print("Объем =", a**3)
# print("Площадь полной поверхности =", 6*a**2 )
# a=int(input())
# b=int(input())
# f=3*(a+b)**3 + 275*b**2-127*a-41
# print(f)
# a=int(input())
# b=a+1
# c=a-1
# print("Следующее за числом", a, "число:", b)
# print("Для числа", a,  "предыдущее число:", c)
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# sum=a+b+c+d
# print(sum*3)
# b=int(input())
# q=int(input())
# n=int(input())
# print(b*(q**(n-1)))
# a=int(input())
# if a%2==0:
#     print(a//2)
# else:
#  print((a//2)+1)
# b=int(input())
# print(b//a)
# print(b%a)
# a=int(input())
# print("Сумма цифр =", (a//100)+(a%10)+((a%100)//10) )
# print("Произведение цифр =", (a//100)*(a%10)*((a%100)//
# b=int(input())
# print("Цифра в позиции тысяч равна", b//1000,
# "\n Цифра в позиции сотен равна" ,((b%1000)//100),
# "\nЦифра в позиции десятков равна", ((b%100)//10),
# "\nЦифра в позиции единиц равна " ,((b%10)))
# a=input()
# b=input()
# if a==b:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")
# a=int(input())
# b=int(input())
# c=int(input())
# # d=int(input())
# if a>0 and b>0 and c>0:
#     print(a+b+c)
# elif a>0 and b>0 and c<0:
#     print(a+b)
# elif a>0 and b<0 and c>0:
#     print(a+c)
# elif a<0 and b>0 and c>0:
#     print(b+c)
# a= int(input())
# if a==0:
#     print("зеленый")
# elif 1<=a<=10:
#     if a%2==0:
#      print("черный")
#     if a%2!=0:
#         print("красный")
# elif 11<=a<=18:
#     if a%2==0:
#         print("красный")
#     if a%2!=0:
#         print("черный")
# elif 19<=a<=28:
#     if a%2==0:
#      print("черный")
#     if a%2!=0:
#         print("красный")
# elif 29<=a<=36:
#     if a%2==0:
#      print("красный")
#     if a%2!=0:
#         print("черный")
# else:
#     print("ошибка ввода")3

# p1, p2, q1, q2 =abs(int(input())), abs(int(input())), abs(int(input())), abs(int(input()))
# print((abs(p1-q1))+(abs(p2-q2)
#
# import math
# # x1=float(input())
# # y1=float(input())
# # x2=float(input())
# R=float(input())
# S=math.pi*R**2
# C=2*math.pi*R
# print(S)
# print(C)
# a= int(input()) 1esep
# if 1500<=a<=2700:
"""
2
"""
# F=int(input())
# C=int(input())
# print("Цельсия =", (F-32)//1.8)
# print("Фаренгейт=", (C*1.8)+32)
# print(C/5, (F-32)/9)
# import random 3esep
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
# if count >
#     average = total_sum / count
#     print(total_sum)
#     print(average)
# else:
#     print("Сан енгізілген жоқ")
# a= float(input())
# b=float(input())
# c=(a+b)/2
# f=math.sqrt(a*b)
# d=(2*a*b)/(a+b)
# s=math.sqrt((a**2+b**2)/2)
# print(c)
# print(f)
# print(d)
# print(s)
# x1,x2= int(input()), int(input())
# y1,y2= int(input()),int(input())
# if (x1+y1)%2==(x2+y2)%2==0:
#     print("YES")
# else:
#     print("NO")
# x = float(input())
# x_rad = math.radians(x)
# result = math.sin(x_rad) + math.cos(x_rad) + math.tan(x_rad) ** 2
# print(result)
# x=float(input())
# c=math.floor(x)
# d=math.ceil(x)
# print(c+d)
# a = float(input())
# b = float(input())
# c = float(input())
# discriminant = b**2 - 4*a*c
# if discriminant > 0:
#     root1 = (-b + math.sqrt(discriminant)) / (2*a)
#     root2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print(f"{root1:.6f}\n{root2:.6f}")
# elif discriminant == 0:
#     root = -b / (2*a)
#     print(f"{root:.6f}")
# else:
#     print("Нет корней")
# import math
# n=int(input())
# a=float(input())
# S=(n*a**2)/(4*math.tan(math.pi/n))
# print(S)
# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')
# num = int(input())
# a = num //1000
# b = (num % 1000) // 100
# c = (num %100)//10
# d= (num%10)
# if a>b and c>b and d>b:
#     print(b)
# elif b>a and c>a and d>a:
#     print(a)
# elif c>
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[s%7==0])
# s=str(input())
# s2=s[::-1]
# if s==s2:
#     print("YES")
# else:
#     print("NO")
# s=str(input())
# print(len(s))
# print(s*3)
# print(s[:1])
# print(s[0:3])
# print(s[23:])
# print(s[::-1])
# print(s[1:26])
# s=str(input())
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])
# s=str(input())
# s2=len(s)
# middle=s2//2
# if s2%2==0:
#     first_part = s[:middle]
#     second_part = s[middle:]
# else:
#     first_part = s[:middle + 1]
#     second_part = s[middle + 1:]
# result_text = second_part + first_part
# print(result_text)
# a=str(input())
# print(a.swapcase())
# if (a==a.title()):
#     print("Yes")
# else:
#     print("No")
# a=str(input())
# if "хорош" in a.lower():
#     print("YES")
# else:
#     print("NO")
# a=str(input())
# count=0
# if a in a.lower:
#     count+=1
#     print(count)
# else:
#     print("no")
# s = 'I learn Python language. Python - awesome!'
# # print(s.find('Python'))
# n = int(input())
#
# # Счетчик сообщений, в которых содержится число 11 минимум 3 раза
# count_messages = 0
#
# # Цикл для обработки каждого сообщения
# for _ in range(n):
#     message = input()
#
#     # Подсчитываем количество вхождений "11" в текущем сообщении
#     count_11 = message.count('11')
#
#     # Если число вхождений больше или равно 3, увеличиваем счетчик сообщений
#     if count_11 >= 3:
#         count_messages += 1
#
# # Выводим результат
# print(count_messages)
print(ord('foo'))