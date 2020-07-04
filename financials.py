class Activities:
    def __init__(self, activity, amount):
        self.activity = activity
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return self.activity

    def salaryAfterActivity(self, income):
        return income - self.amount 

    
    
class Food(Activities):
    def __init__(self, activity, amount):
        super().__init__(activity, amount)
        self.cart_item = []
        self.cart_price = []

    def food_list_items(self, **kwargs):
        for key, value in kwargs.items():
            self.cart_item.append(key)
            self.cart_price.append(value)

    def item_cart(self):
        return self.cart_item
    
    def price_cart(self):
        return self.cart_price

    def salaryAfterFood(self, income):
        return income - self.amount
        # sum(self.cart_price)


class Bills(Activities):
    def __init__(self, activity, amount):
        super().__init__(activity, amount)
        self.bill_name = []
        self.bill_price = []

    def bill_list(self, **kwargs):
        for key, value in kwargs.items():
            self.bill_name.append(key)
            self.bill_price.append(value)
            return key + value
    def name_bill(self):
        return self.bill_name
    
    def price_bill(self):
        return self.price_bill

    def salaryAfterBills(self, income):
        return income - self.amount

class Saveings(Activities):
    def __init__(self, activity, amount):
        super().__init__(activity, amount)

    def saveing_time(self,income):
        return (self.amount / income ) 

    def saveing_amount(self, monney_in_bank):
        if self.amount < monney_in_bank:
            return f'you dont need to save any?: '
        else:
            return self.amount - monney_in_bank


