class Student:
    identification: int
    name: str
    age: int
    semester: int
    grades: list[float]

    def __init__(self, att_identification: int, att_name: str, att_age: int, att_semester: int, att_grades: list[float]) -> None:
        self.identification = att_identification
        self.name = att_name
        self.age = att_age
        self.semester = att_semester
        self.grades = att_grades

    def get_average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def view_info(self) -> str:
        average = self.get_average()
        return f"Name: {self.name}, Age: {self.age}, Semester: {self.semester}, Average: {average}"

students: list[Student] = []

while True:
    op = int(input("""Choose
    1. Enter data
    2. view a student's average
    3. view a student's information
    0. Exit
    : """))


    if op == 0:
        break

    if op == 1:
        identification = int(input("Enter the ID: "))
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        semester = int(input("Enter the semester: "))
        grades = [float(input(f"Enter grade {i+1}: ")) for i in range(3)]
        student = Student(identification, name, age, semester, grades)
        students.append(student)

    elif op == 2 or op == 3:
        identification = int(input("Enter the ID: "))
        for student in students:
            if student.identification == identification and op == 2:
                average = student.get_average()
                print(f"The average of {student.name} is: {average}")
            elif student.identification == identification and op == 3:
                info = student.view_info()
                print(info)

    else:
        for student in students:
            print(student)
            print(f"Identification: {student.identification}, Name: {student.name}, Age: {student.age}, Semester: {student.semester}, Grades: {student.grades}")