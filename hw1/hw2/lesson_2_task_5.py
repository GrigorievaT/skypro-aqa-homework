#Месяц — сезон
def month_to_season(num):
    if num > 12 or num < 1:
        print("Введите корректный номер месяца (число от 1 до 12)")
    if num == 1 or num == 2 or num ==12:
        print("Зима")
    elif num == 3 or num == 4 or num == 5:
        print("Весна")
    elif num == 6 or num == 7 or num == 8:
        print("Лето")
    elif num == 9 or num == 10 or num == 11:
        print("Осень")

n=input("Введите номер месяца, мы определим сезон: ")
num=int(n)
month_to_season(num)