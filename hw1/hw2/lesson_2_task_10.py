#Банковское приложение*
def bank(x, y):
    for i in range(1, y+1):
        sum = x + x*0.1
        x = sum
    print("Через ", y, "лет на счету будет ", sum, "рублей")
x_st = input("Введите размер вклада: ")
x = int(x_st)
y_st = input("Введите срок вклада: ")
y = int(y_st)
bank(x, y)
