# Define the Employee class
class Employee:

    # Initialize the attributes
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    # A method to give the employee a raise
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} got a raise of ${amount}. New salary is ${self.salary}.")

    # A method to display the employee's information
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")

# Create objects of the Employee class
employee1 = Employee("John Doe", "12345", 60000)
employee2 = Employee("Jane Smith", "67890", 65000)

# Use the methods of the objects
employee1.display_info()
# Output:
# Employee Name: John Doe
# Employee ID: 12345
# Salary: $60000

employee2.display_info()
# Output:
# Employee Name: Jane Smith
# Employee ID: 67890
# Salary: $65000

employee1.give_raise(5000)
# Output:
# John Doe got a raise of $5000. New salary is $65000.
