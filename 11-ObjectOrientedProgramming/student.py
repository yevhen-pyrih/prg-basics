# class definition
class Student():
    def __init__(self, name="", age=0, sex=""):
        self.name = name
        self.age = age
        self.sex = sex

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.sex = "male"
    student2.name = "Olivia"
    student2.age = 21
    student2.sex = "female"

    student3 = Student("Yevhen", 17, "male")

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name} is {student1.sex}, {student1.age} years old')
    print(f'{student2.name} is {student2.sex}, {student2.age} years old')
    print(f'{student3.name} is {student3.sex}, {student3.age} years old')

if __name__ == "__main__":
    main()