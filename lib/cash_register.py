#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0 
    self.discount = discount # in percentage, e.g., 20 for 20%
    self.items = [] # List to track all items added
    self.last_transaction = None #To void last transaction

  def add_item(self, name, price, quantity = 1):
    item_total = price * quantity
    self.total += item_total
    self.items += [name] * quantity
    self.last_transaction = {"name": name, "price": price, "quantity": quantity, "total": item_total}

  def apply_discount(self):
    if self.discount > 0:
       discount_amount = self.total * (self.discount/100)
       self.total -= discount_amount
       print (f"After the discount, the total comes to ${int(self.total)}.")
    else: 
       print ("There is no discount to apply.")
  
  def void_last_transaction(self):
    if self.last_transaction:
      self.total -= self.last_transaction["total"]
      self.items.pop()
      self.last_transaction = None
      return "Last transaction voided."
    else:
      return "No transaction to void"
  
  def list_items(self):
    return self.items
  
  def get_total(self):
    return(self.total, 2)