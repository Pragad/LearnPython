#! /usr/bin/env/python

#-------------------------------------------------------------------------------------------
# Class 1
#-------------------------------------------------------------------------------------------
class Employee:
    'Employee Generic Class'

    # This is like a Static Variables that counts all employees
    numEmployees = 0

    def __init__(self, name, age = 1):
        self.name = name
        self.age = age

        # NumEmployees can be accessed only through Employee
        Employee.numEmployees += 1

    def getEmployeesCount(self):
        print("Number of People: ", Employee.numEmployees)
        return Employee.numEmployees

    def printEmployee(self):
        print("Name: %s, Age: %d" % (self.name, self.age))

#-------------------------------------------------------------------------------------------
# Class 2
#-------------------------------------------------------------------------------------------
class Shapes:
    'Shapes Generic Class'

    # This is like a Static Variables that counts all shapes
    numShapes = 0


#-------------------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------------------
def main():
    print("Basic Class")

    #Employee Example
    emp1 = Employee("abc", 23)
    emp2 = Employee("def", 34)
    emp3 = Employee("qwe", 98)

    # Calling with Default AGE
    emp4 = Employee("qwe")
    empList = [emp1, emp2, emp3, emp4]

    print(Employee.numEmployees)
    for emp in empList:
        emp.printEmployee()

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

