#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self._discount = 0
        self.discount = discount  # goes through setter

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Must be an integer between 0-100
        if type(value) is not int:
            print("Not valid discount")
            return
        if value < 0 or value > 100:
            print("Not valid discount")
            return
        self._discount = value

    def add_item(self, item, price, quantity=1):
        if quantity is None:
            quantity = 1
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0 or len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return
        # Apply percentage off
        self.total = int(self.total * (100 - self.discount) / 100)
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return
        
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        
        # Remove items - remove last occurrence(s)
        for _ in range(last["quantity"]):
            for i in range(len(self.items) - 1, -1, -1):
                if self.items[i] == last["item"]:
                    del self.items[i]
                    break