class student:
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def say_hello(self):
        print(self.name)
    def introduce(self):
        print(self.age)

student1=student("Kiran", 21)
student2=student("Ravi", 22)

student1.say_hello()
student1.introduce()

student2.say_hello()
student2.introduce()
