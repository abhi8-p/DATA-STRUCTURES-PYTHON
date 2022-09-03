'''
Here instead of super we are directly using class name to call the constructors/functions for the parent class
NOTE: self should mandatorily be used in the Child while calling the Parent's method
But how to know in main func only <obj name>.<same func>(student.my_name()) is called
-> MRO method resolution operator, It decides which function will be called when function is invoked and also which function to call when there is a conflict.
Here Person's my_name will be called as it is first Parent class,
If we change the order then Athelete class's my_name will be called
'''
class Person():
    def __init__(self,name,age):
        self.name =name
        self.age = age
    
    def my_name(self):
        print("My name is",self.name)

class Athelete():
    def __init__(self,teacher):
        self.teacher = teacher

    def my_name(self):
        print("My name is",self.teacher)

# class Student(Person,Athelete):
class Student(Athelete,Person):
    def __init__(self, name, age,id,gpa,teacher):
        Person.__init__(self,name, age)
        Athelete.__init__(self,teacher)

        #calling my_name func
        Person.my_name(self) 
        Athelete.my_name(self)

        self.gpa =gpa
        self.id= id

student  = Student("Abhis",23,1234,4.5,"Abhishek")
print(student.name)
print(student.age)
print(student.id)
print(student.gpa)
print(student.teacher)
student.my_name()