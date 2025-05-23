class Perfume:
    def __init__(self, name, brand, price, currency, concentration, gender, season, types):
        self.name = name.strip()
        self.brand = brand.strip()
        self.price = price
        self.currency = currency
        self.concentration = concentration
        self.gender = gender
        self.season = season
        self.types = types

    def validate(self):
        if not self.name:
            raise ValueError("Perfume name is required.")
        if not self.brand:
            raise ValueError("Brand is required.")
        if not isinstance(self.price, (int, float)) or self.price <= 0:
            raise ValueError("Price must be a positive number.")
        if not self.currency:
            raise ValueError("Currency is required.")
        if not self.concentration or not isinstance(self.concentration, list) or len(self.concentration) != 1:
            raise ValueError("Exactly one concentration must be selected.")
        if not self.gender:
            raise ValueError("Gender is required.")
        if not self.season or not isinstance(self.season, list):
            raise ValueError("At least one season must be selected.")
        if not self.types or not isinstance(self.types, list):
            raise ValueError("At least one type must be selected.")

    def to_dict(self):
        return {
            "name": self.name,
            "brand": self.brand,
            "price": self.price,
            "currency": self.currency,
            "concentration": self.concentration,
            "gender": self.gender,
            "season": self.season,
            "types": self.types
        }
