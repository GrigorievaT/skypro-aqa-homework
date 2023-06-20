#Площадь квадрата
import math
def square(a1):
    s=a1*a1
    s1=math.ceil(s)
    print("Площадь квадрата = ", s1)
a=input("Введите сторону квадрата: ")
a1=float(a)
square(a1)
