from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Redmi Note 14", "+79157722533"),
    Smartphone("Samsung", "Galaxy S25", "+79265430422"),
    Smartphone("Honor", "X6C", "+79161990488"),
    Smartphone("Apple", "iPhone 16 Pro", "+79263240158"),
    Smartphone("Infinix", "Zero Flip", "+79164990282")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")