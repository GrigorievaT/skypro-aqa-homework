#Функция печатает числа от 1 до n. При этом: 
#1. если число делится на 3, печатать `Fizz`;
#2. если число делится на 5, печатать `Buzz`;
#3. если число делится на 3 и на 5, печатать `FizzBuzz`.
def fizz_buzz(n):
   for i in range(1, n):
      if  i % 3 ==0 and i % 5 ==0:
         print("FizzBuzz")
      elif i % 3 == 0: 
         print("Fizz")
      elif i % 5 ==0:
         print("Buzz")
      else: 
         print(i)

n_st=input("Введите число n:")
n=int(n_st)+1
fizz_buzz(n)

