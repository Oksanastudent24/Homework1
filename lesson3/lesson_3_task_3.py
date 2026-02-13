from address import Address
from mailing import Mailing

to_address = Address("142620", "Кострома", "Комсомольская", "17", "4")
from_address = Address("117133", "Москва", "Академика Варги", "2", "257")

mailing = Mailing(to_address, from_address, 5000, "AB777777777RU")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")