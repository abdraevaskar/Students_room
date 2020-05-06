class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Major: {self.major}'

Steve = Student('Steven Shultz', 23, 'English')
print(Steve)
print()
Johnny = Student('Jonathan Rosenberg', 24, 'Biology')
print(Johnny)
print()
Penny = Student('Penelope Meramveliotakis', 21, 'Physics')
print(Penny)