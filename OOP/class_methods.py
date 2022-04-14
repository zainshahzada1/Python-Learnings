import csv
class Item:
    pay_rate = 0.8  # class level
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Assert
        assert price>=0
        assert quantity>=0
        self.name = name  # instance level
        self.price = price  # instance level
        self.quantity = quantity  # instance level
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                item.get('name'),
                float(item.get('price')),
                int(item.get('quantity'))
            )

    def __repr__(self):
        return f"Item('{self.name},'{self.price},'{self.quantity}')"


Item.instantiate_from_csv()
print(Item.all)
  