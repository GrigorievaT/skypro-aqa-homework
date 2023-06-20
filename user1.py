class User:

    age = 0
    def __init__(self, name): #конструктор, создание класса
        print("я создался")
        self.username=name

    def sayName(self): #метод
        print("меня зовут ", self.username)

    def sayAge(self): #метод
        print("Твой возраст ", self.age)

    def setAge(self, newage):
        self.age = newage
        print("Новый возраст ", newage)

