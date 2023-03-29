"""WeCare insurance company wants to calculate premium of vehicles.

-->Vehicles are of two types - "Two Wheeler" and "Four Wheeler Each vehicle is
identified by vehicle id, type, cost and premium amount.

-->Premium amount is 2% of the vehicle cost for two wheelers and6% of the
vehicle cost for four wheelers.

Calculate the premium amount and display the vehicle details. Write a Python
program to implement the class chosen with its attributes and methods.

Note:

Consider all instance variables to be private and methods to be public

Include getter and setter methods for all instance variables Display appropriate error message,
if the vehicle type is invalid.

Perform case sensitive string comparison

Represent few objects of the class, initialize instance variables using setter methods,
invoke appropriate methods and test your program."""
def check_type(type):
    vehicle_type=['Two Wheeler','Four Wheeler']
    if type not in vehicle_type:
            return 0
    return 1
class Vehicle:
    def __init__(self):
        self._vehicle_cost=None
        self._vehicle_id=None
        self._vehicle_type=None
        self._premium_amount=None
        
    def set_vehicle_id(self,vehicle_id):
        self._vehicle_id=vehicle_id
    def set_vehicle_type(self,vehicle_type):
        if check_type(vehicle_type):
            self._vehicle_type=vehicle_type
        else:
            return "invalid Vehicle DETAILS"
    def set_vehicle_cost(self,vehicle_cost):
        self._vehicle_cost=vehicle_cost
    def get_vehicle_id(self):
        return self._vehicle_id
    def get_vehicle_type(self):
        return self._vehicle_type
    def get_vehicle_cost(self):
        return self._vehicle_cost
    def set_premium_amount(self,premium_amount):
        self._premium_amount=premium_amount
    def get_premium_amount(self):
        return self._premium_amount
        
    def calculate_premium(self):
        if self._vehicle_type=="Two Wheeler":
            self._premium_amount=self._vehicle_cost*2/100
        elif self._vehicle_type=="Four Wheeler":
            self._premium_amount=self._vehicle_cost*6/100
        else:
            print("Invalid Vehicle Type")
            
    def display_vehicle_details(self):
        print("premium:",self._premium_amount)
        print("type:",self._vehicle_type)
        print("cost:",self._vehicle_cost)
    
v1 = Vehicle()
#v1.set_vehicle_id=10
v1.set_vehicle_type("Two Wheeler")
v1.set_vehicle_cost(95000)
v1.calculate_premium()
v1.display_vehicle_details()
v2 = Vehicle()
v2.set_vehicle_type("Four Wheeler")
v2.set_vehicle_cost(405000)
v2.calculate_premium()
v2.display_vehicle_details()



