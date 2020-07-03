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


class Bills(Activities):
    def __init__(self, activity, amount):
        super().__init__(activity, amount)


class Saveings(Activities):
    def __init__(self, activity, amount):
        super().__init__(activity, amount)

    
a = Activities('football', 500)

print(a.subtract_income(1000))


