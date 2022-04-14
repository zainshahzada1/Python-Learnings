class Item :
    pay_rate=0.8    #class level
    def __init__(self,name:str,price:float,quantity=0):
        self.name=name  #instance level
        self.price=price    #instance level
        self.quantity = quantity  # instance level
    def calculate_total_price(self):
        return self.price*self.quantity
    def apply_discount(self):
        self.price = self.price*self.pay_rate
item1=Item("Laptop",100,1)
item2=Item("Phone",1000,3)
# print(item1.__dict__)  # returns a dictionary having instance level attributes
item1.apply_discount()
print (item1.price)
item2.pay_rate=0.7
item2.apply_discount()
print (item2.price)
