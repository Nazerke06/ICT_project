# a = int(input())
# if  a>90:
#     print("A")
# elif 80<a<=90:
#     print("B")
# elif 60<=a<=80:
#     print ("C")
# else:
#     print("D")
# a=int(input())
# if a%2==0:
#     print("jup")
# else:
#     print("tak")
# a=0
# while a<6:
#  a += 1
#  if a==3 :
#   continue
#  print(a
# task1
# def km_to_miles(m):
#     n=m*1000
#     print(n)
# km_to_miles(int(input()))
# task2
# def  is_divisable_by_11(n):
#    if  n%11==0:
#        print("YES")
#    else:
#        print("NO")
# is_divisable_by_11(int(input()))
# def get_highest (n,m):
#     if n>m:
#        print(n)
#     elif n<m:
#         print(m)
#     else:
#         print("equal")
# get_highest(int(input()), int(input()))
# import math
# def  hexagon_area(a):
#     S=math.sqrt(3)/4*a**2
#     print(S)
# hexagon_area(float(input()))
# def Sleeps_until_xmas(n,v):
#     xday=n*v-31*12
#     print(xday)
# task6
# def  is_palindrone(s):
#     a= s[::-1]
#     if s==a:
#         print("yes")
#     else:
#          print("No")
# is_palindrone(str(input()))
# def  Fuel_cost(n):
#     g=n*50
#     litr=g*3.79
#     cost=litr*1
#     print(cost)
# Fuel_cost(float(input()))
# def tri_recursion (n):
# array=[1,3,5,7]
# array.append(9)
# array.append(11)
# print(array)
# array=[1, 3, 5, 3, 7, 1, 9, 3]
# array.reverse()
# print(array)
# n = 4
# array = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             array[i][j] =1
#         elif i < j:
#             array[i][j] =0
#         else:
#             array[i][j] =2
# for row in array:
#     print(*row)
# x=lambda a:a+15
# print(x(10))
# def myfunc(n):
#     return lambda b:b*n
# mydoubler=myfunc(6)
# print(mydoubler(8))
