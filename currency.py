class Currency:
    def __init__(self, currency):
        self.currency = currency

    def __str__(self):
        if self.currency.isalpha() == False and self.currency.isdigit() == False:
            return self.currency
        else:
            return '$'
    