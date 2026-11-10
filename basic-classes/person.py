class Person:

    def __init__(self, att_name: str, att_age: int, at_gender: str) -> None:
        self.__name: str = att_name
        self.age: int = att_age
        self.gender: str = at_gender

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str) -> None:
        if len(value) > 1:
            self.__name = value
        else:
            print("You cannot assign this value.")

p1 = Person("Alice", 30, "Female")

p1.Name = "B"

print(p1.Name)