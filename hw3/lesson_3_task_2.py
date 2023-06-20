#Задание 2. Список объектов
from smartphone import Smartphone
el = Smartphone("Redmi", "Note", "+79998886655")
el2 = Smartphone("Nokia", "A10", "+71112223344")
elem1 = el.marka+"-"+el.model+"."+el.number
elem2 = el2.marka+"-"+el2.model+"."+el2.number
elem3 = el.marka+"-"+el2.model+"."+el.number
elem4 = el2.marka+"-"+el.model+"."+el.number
elem5 = el.marka+"-"+el.model+"."+el2.number
catalog = [elem1, elem2, elem3, elem4, elem5]
for i in range(0, 5):
    print(catalog [i])






