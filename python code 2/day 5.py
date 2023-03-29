"""class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "Shoe with price:" + str(self.price) + "and material:" +self.material
    s1=Shoe(1000,"Canvas")
    print(s1)
-->class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("Calculating price")
Mobile().purchase()
-->class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id= cust_id
        self.name= name
        self.age =age
        self.wallet_balance= wallet_balance
    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
            print("The balance is ",self.wallet_balance)
c1=Customer(108, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance
-->class Dam:
    def __init__(self, name, length):
        self.name=name
        self._length=length
    def get_length(self):
        return self._length
    dam1= Dam("ABC dam", 3.5)
    print("Dam name:",dam1.name)
    print("Dam Length",dam1.length())
-->class Table:
    def _init_(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top, wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False,True)
print(rate)"""
class Table:
    def _init_(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table() #
front_table=back_table
back_table=dining_table
print(dining_table, back_table,front_table)

    
