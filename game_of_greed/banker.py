  # shelf instance method - temporarily stores un-banked points. Input of amount of points
  # balance - total of points    shelved - un-banked points

class Banker():

  def __init__(self, shelved=0, balance=0):
    self.balance = balance
    self.shelved = shelved
    pass


  def shelf(self, points):
    self.shelved +=points
      
  
  def bank(self):
    self.balance = self.shelved
    self.shelved = 0
    pass
  # bank instance method - adds any points on the shelf to total and resets shelf to 0

# clear shelf method to remove un-banked points
  def clear_shelf(self):
    self.shelved = 0