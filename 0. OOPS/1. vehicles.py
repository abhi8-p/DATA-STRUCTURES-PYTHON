from inspect import Parameter


class Vehicles:
    wheels =6
    def __init__(self):#,type,id,cost):
        # self.type = type
        # self.id = id
        # self.cost = cost
        # if type == "Two Wheeler":
        #     self.premium = 0.02 * cost
        # elif type == 'Four Wheeler':
        #     self.premium = 0.06 * cost 
        pass

    def get_details(self):
        print("Premium of your {} vehicle is: {}".format(self.type, self.premium))

    def set_wheels(self):
        Vehicles.wheels = 9

    @classmethod
    def change_wheels(cls,n_wheels):
        cls.wheels = n_wheels

    
    @staticmethod
    def static_change_wheels(n_wheels):
        Vehicles.wheels = n_wheels

def main():
    # type = input("Enter your Vehicle type: ")
    # id = input("Enter your vehicle ID: ")
    # cost = float(input("Enter your vehicle price: "))
    print(Vehicles.wheels)
    Vehicles.change_wheels(7)
    print(Vehicles.wheels)
    Vehicles.static_change_wheels(8)
    print(Vehicles.wheels)
    c = Vehicles()
    c.set_wheels()
    print(Vehicles.wheels)
    
            

#driver code......
if __name__ == '__main__':
    main()
    