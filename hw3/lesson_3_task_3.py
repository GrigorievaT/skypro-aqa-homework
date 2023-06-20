#Задание 3. Вложенные классы
from mailing import Mailing
toA = Mailing.toAdress.to_address.city
fromA = Mailing.toAdress.from_address.city
post = Mailing(toA, fromA, "1000", "12345678998745")
print("Отправление", post.track, "из", Mailing.toAdress.to_address.index, Mailing.toAdress.to_address.city, Mailing.toAdress.to_address.street, Mailing.toAdress.to_address.house, "-", Mailing.toAdress.to_address.apartament, "в", Mailing.toAdress.from_address.index, Mailing.toAdress.from_address.city, Mailing.toAdress.from_address.street, Mailing.toAdress.from_address.house, "-", Mailing.toAdress.from_address.apartament, ".", "Стоимость", post.cost, "рублей.")
