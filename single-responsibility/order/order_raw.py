class Order():
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def calculate_total_price(self):
        order_total = 0
        for i in range(len(self.prices)):
            order_total += self.quantities[i] * self.prices[i]
        
        return order_total

    def apply_payment(self, payment_type, cvv):
        if payment_type == 'credit':
            print('Processing credit payment')
            print(f'Verifying CVV: {cvv}')
            self.status = 'paid'
        elif payment_type == 'debit':
            print('Processing debit payment')
            print(f'Verifying CVV: {cvv}')
            self.status = 'paid'
        else:
            raise Exception(f'Invalid payment type: {payment_type}')