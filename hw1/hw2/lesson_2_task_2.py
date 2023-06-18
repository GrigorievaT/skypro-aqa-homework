#Високосный год
def is_year_leap(year):
    if year % 4 == 0:
        print("год ", year, ":", True)
    else:
        print("год ", year, ":", False)

year_st=input("Введите год: ")
year=int(year_st)
is_year_leap(year) 

   
