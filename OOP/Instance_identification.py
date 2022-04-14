class Item:
    pay_rate = 0.8  # class level
    all=[]
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name  # instance level
        self.price = price  # instance level
        self.quantity = quantity  # instance level
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate

    def __repr__(self):
        return f"Item('{self.name},'{self.price},'{self.quantity}')"


item1 = Item("Laptop", 1000, 2)
item2 = Item("Phone", 100, 3)
item3 = Item("Computer", 2000, 5)
item4 = Item("Router", 50, 6)
item5 = Item("Charger", 10, 4)
 
print (Item.all)
