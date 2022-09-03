'''
Here if Parent and Grand Parent class has same function then the immediate Parent's function will be called.
'''
class Athelete():
    def __init__(self,teacher):
        self.teacher = teacher

    def my_name(self):
        print("My name is",self.teacher)

class Person(Athelete):
    def __init__(self,name,age):
        self.name =name
        self.age = age
    
    def my_name(self):
        print("My name is",self.name)

class Student(Person):
    def __init__(self, name, age,id,gpa,teacher):
        Person.__init__(self,name, age)

        self.gpa =gpa
        self.id= id

def main():
    student  = Student("Abhis",23,1234,4.5,"Abhishek")
    print(student.name)
    print(student.age)
    print(student.id)
    print(student.gpa)
    print(student.teacher)
    student.my_name()


#driver code......
if __name__ == '__main__':
    main()
    