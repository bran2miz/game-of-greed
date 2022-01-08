#   # shelf instance method - temporarily stores un-banked points. Input of amount of points
#   # balance - total of points    shelved - un-banked points

# class Banker():

#   def __init__(self):
#     self.balance = 0
#     self.shelved = 0
#     pass


#   def shelf(self, points):
#     self.shelved +=points
#     return self.shelved
      
  
#   def bank(self):
#     self.balance += self.shelved
#     self.shelved = 0
#     return self.balance
#   # bank instance method - adds any points on the shelf to total and resets shelf to 0

# # clear shelf method to remove un-banked points
#   def clear_shelf(self):
#     self.shelved = 0

class Banker:
    """Banker is reponsible for tracking points "on the shelf" and "in the bank"
    version_1
    """
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amt):
        self.shelved += amt

    def clear_shelf(self):
        self.shelved = 0