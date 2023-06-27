#Калькулятор
class Calculator:

    def sum(self, a, b): #функция сложения
        return a+b
    
    def sub(self, a, b): #функция вычитания
        return a-b
    
    def mul(self, a, b): #функция умножения
        return a*b
       
    def div(self, a,b): #функция деления
        if (b ==0): # прверка деления на 0
            raise ArithmeticError("На ноль делить нельзя")
        return a/b

    def pow(self, a, b=2): #функция возведения в степень
        return a**b
    
    def avg(self, nums): #функция нахождения среднего арифметического
        if (len(nums) ==0): # проверка пустого списка
            return 0
        s = 0
        for num in nums:
            s = self.sum(s, num)
        l = len(nums)
        return self.div(s, l)
