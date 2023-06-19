#Площадь квадрата
def square(a1):
    s=a1*a1
    import math
    s1=math.ceil(s)
    print("Площадь квадрата = ", s1)
a=input("Введите сторону квадрата: ")
a1=float(a)
square(a1)
