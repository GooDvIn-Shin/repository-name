from address import Address
from mailing import Mailing

to_adr = Address("105000", "Москва", "Маяковская", "10", "25")

from_adr = Address("680050", "Санкт-Петербург", "Неделина", "3", "12")

shipment = Mailing(
    to_address=to_adr,
    from_address=from_adr,
    cost=350,
    track="RU123456789"
)

print(
    f"Отправление {shipment.track} из "
    f"{shipment.from_address.index}, "
    f"{shipment.from_address.city}, "
    f"{shipment.from_address.street}, "
    f"{shipment.from_address.house} - "
    f"{shipment.from_address.apartment} в "
    f"{shipment.to_address.index}, "
    f"{shipment.to_address.city}, "
    f"{shipment.to_address.street}, "
    f"{shipment.to_address.house} - "
    f"{shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)
