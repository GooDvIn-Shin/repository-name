from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79111111111"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79222222222"))
catalog.append(Smartphone("Xiaomi", "14 Pro", "+79333333333"))
catalog.append(Smartphone("Google", "Pixel 8", "+79444444444"))
catalog.append(Smartphone("Huawei", "Pura 70", "+79555555555"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
