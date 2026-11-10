# Person class
class Person():
    name: str = ""
    age: int = 0
    height: float = 0.0
    gender: str = ""

    def __init__(self, att_name: str, att_age: int, att_height: float, att_gender: str) -> None:
        self.name = att_name
        self.age = att_age
        self.height = att_height
        self.gender = att_gender

    def walk(self) -> str:
        return f"Hi, I'm {self.name} and I'm walking."

# person1 -> Object   Person() -> Class
# person1 = Person("Juan", 25, 1.75, "Male")
# person2 = Person("María", 23, 1.65, "Female")
# print(person1.name)
# print(person2.name)
# print(person1.walk())
# print(person2.walk())

people: list[Person] = []

while True:
    op = int(input("""Choose
    1. Enter data
    2. view list of people
    0. Exit
    : """))

    if op == 0:
        break

    if op == 1:
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        height = float(input("Enter the height: "))
        gender = input("Enter the gender: ")

        person = Person(name, age, height, gender)
        people.append(person)

    else:
        for person in people:
            print(person)
            print(f"Name: {person.name}, Age: {person.age}, Height: {person.height}, Gender: {person.gender}")