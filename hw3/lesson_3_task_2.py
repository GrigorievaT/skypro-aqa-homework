#Задание 2. Список объектов
from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Redmi", "Note", "+79998887766"))
catalog.append(Smartphone("Nokia", "A10", "+71112223344"))
catalog.append(Smartphone("Samsung", "A20", "+72223334455"))
catalog.append(Smartphone("Apple", "13", "+73334445566"))
catalog.append(Smartphone("Poco", "F5", "+74445556677"))
for i in catalog:
    print(i.marka, i.model, i.number)





