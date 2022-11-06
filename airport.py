class Airport:
    def __init__(self, code, name, country, city, lat, lon, rate) -> None:
        self.code = code
        self.name = name
        self.country = country
        self.city = city
        self.lat = lat
        self.lon = lon
        self.rate = rate

    def __repr__(self) -> str:
        return f"Airport : {self.name} in {self.country}"
