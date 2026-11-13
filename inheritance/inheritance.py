# Parent
class Vehicle:
    def __init__(self, brand: str, model: str) -> None:
        self.brand: str = brand
        self.model: str = model

    def show_info(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}"

# Parent
class Electric:
    def __init__(self, battery_capacity: int) -> None:
        self.battery_capacity: int = battery_capacity

    def show_info(self) -> str:
        return f"Battery capacity: {self.battery_capacity} kWh"

# Child
class Car(Vehicle):
    def __init__(self, brand: str, model: str, doors: int) -> None:
        super().__init__(brand, model)
        self.doors: int = doors

    def show_info(self) -> str:
        return f"{super().show_info()}, Doors: {self.doors}"

# Child
class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, type: str) -> None:
        super().__init__(brand, model)
        self.type: str = type

    def show_info(self) -> str:
        return f"{super().show_info()}, Type: {self.type}"

# Multiple inheritance
class ElectricCar(Car, Electric):
    def __init__(self, brand: str, model: str, doors: int, battery_capacity: int) -> None:
        Car.__init__(self, brand, model, doors)
        Electric.__init__(self, battery_capacity)

    def show_info(self) -> str:
        return f"{Car.show_info(self)}, {Electric.show_info(self)}"

# Multilevel inheritance
class Truck(Car):
    def __init__(self, brand: str, model: str, doors: int, load_capacity: int) -> None:
        super().__init__(brand, model, doors)
        self.load_capacity: int = load_capacity

    def show_info(self) -> str:
        return f"{super().show_info()}, Load capacity: {self.load_capacity} kg"

# Usage example
car1 = Car("Toyota", "Corolla", 4)
motorcycle1 = Motorcycle("Honda", "CBR500R", "Sport")
electric_car1 = ElectricCar("Tesla", "Model 3", 4, 75)
truck1 = Truck("Ford", "F-150", 2, 1000)

print(car1.show_info())
print(motorcycle1.show_info())
print(electric_car1.show_info())
print(truck1.show_info())