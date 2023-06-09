# Define the class
class Student:

    # Initialize the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A method for the student to say hello
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old!")

    # A method for the student to introduce themselves
    def introduce(self):
        print(f"I am a student named {self.name}, and I am {self.age} years old.")

# Create objects of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Use the methods of the objects
student1.say_hello()    # Output: Hello, my name is Alice and I am 20 years old!
student1.introduce()    # Output: I am a student named Alice, and I am 20 years old.

student2.say_hello()    # Output: Hello, my name is Bob and I am 22 years old!
student2.introduce()    # Output: I am a student named Bob, and I am 22 years old.
