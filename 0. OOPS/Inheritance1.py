""" function overriding,
use of super function 
what if parent and child has same variables? then the variable will have last assigned value
best practice is to remove the same variables from the child class
can we call constructor more than once? yes
"""
class base:
    def __init__(self,sides,value):
        print("inside parent constructor")
        self.sides = sides
        self.value = value
    
    def get_total(self):
        print("inside parent get_total")
        print("sides = {}, value = {}".format(self.sides , self.value))
        return self.sides * self.value
        
    def get_updated_total(self):
        print("inside parent get_updated_total")
        return self.sides * self.value
        
class child(base):
    def __init__(self,*args):
        print("inside child constructor")
        self.sides = args[0]
        self.val = args[1]
        super().__init__(args[2],args[3])

    
    def get_total(self):
        print("inside child get_total")
        # self.__init__(30,60,30,80)
        # super().__init__(30,50)
        print("Parent updated get total {}".format(super().get_updated_total()))
        return self.sides * self.val 

print("Instantiation")
c = child(10,20,30,40)
# c.__init__(30,70,30,90)
print("Calling child parent total")
print(c.get_total())