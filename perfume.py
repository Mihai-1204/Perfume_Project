class Perfume:
    def __init__(self, name, brand, price, gender, season, edt, edp, perfume, perfume_type, concentration):
        self.name = name
        self.brand = brand
        self.price = price
        self.gender = gender
        self.season = season
        self.edt = edt
        self.edp = edp
        self.perfume = perfume
        self.type = perfume_type
        self.concentration = concentration

    def to_dict(self):
        return {
            'name': self.name,
            'brand': self.brand,
            'price': self.price,
            'gender': self.gender,
            'season': self.season,
            'edt': self.edt,
            'edp': self.edp,
            'perfume': self.perfume,
            'type': self.type,
            'concentration': self.concentration
        }
