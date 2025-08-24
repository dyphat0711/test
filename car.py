class Car:
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def __str__(self):
        return f"This is a Car named {self.name} with engine {self.engine}."


class Vehicle(Car):
    def __init__(self, name, engine):
        super().__init__(name, engine)
        self.wheel = 4

    def __str__(self):
        return super().__str__() + f" It is a Vehicle and has {self.wheel} wheels."


class Moto(Car):
    def __init__(self, name, engine):
        super().__init__(name, engine)
        self.wheel = 2

    def __str__(self):
        return super().__str__() + f" It is a Moto and has {self.wheel} wheels."


if __name__ == "__main__":
    Yamaha = Moto("R10", "V5")
    Bmw = Vehicle("XM", "V10")

    if isinstance(Bmw, Vehicle):
        print("This is car")

    if Yamaha.engine == "V5":
        print("This car isn't not my type.")

    print(Bmw)
    print(Yamaha)
