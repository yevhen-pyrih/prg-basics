class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age}"
    
person1 = Person("Jonhn Doe", 45)

print(person1)