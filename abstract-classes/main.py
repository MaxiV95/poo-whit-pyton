from abc import ABC, abstractmethod

# Parent
class Vehicle(ABC):
    def __init__(self, brand: str, model: str) -> None:
        self.brand: str = brand
        self.model: str = model

    @abstractmethod
    def accelerate(self) -> str:
        pass

    def show_info(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}"

# Child
class Car(Vehicle):
    def __init__(self, brand: str, model: str, doors: int) -> None:
        super().__init__(brand, model)
        self.doors: int = doors

    def accelerate(self) -> str:
        return f"The car {self.brand} {self.model} is accelerating."

    def show_info(self) -> str:
        return f"{super().show_info()}, Doors: {self.doors}"

# Child
class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, type: str) -> None:
        super().__init__(brand, model)
        self.type: str = type

    def show_info(self) -> str:
        return f"{super().show_info()}, Type: {self.type}"

v1 = Car("Toyota", "Corolla", 4)
print(v1.show_info())
print(v1.accelerate())