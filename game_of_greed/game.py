from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic
# from game_of_greed.game_logic import GameLogic

class Game:

  def __init__(self, rounds =1, dice_quantity = 6):
    self.banker = Banker()
    self.status = True
    self.number_of_rounds = rounds
    self.dice_quantity = dice_quantity

  def play(self, roller = GameLogic.roll_dice):
    self.roll_dice = roller
    print("Welcome to Game of Greed")
    print("(y)es to play or (n)o to decline")
    player_input = input("> ")
    if player_input == 'n':
      print('OK. Maybe another time')
    elif player_input == 'y':
        self.dice_quantity = 6
        self.round_start()

  def round_start(self):
    while self.status and self.banker.balance <= 10000:
      dice_quantity = 6    
      while self.status:
        print(f"Starting round {self.number_of_rounds}")
        print(f"Rolling {self.dice_quantity} dice...")
        dice_string = ' '.join(str(num) for num in (self.roll_dice(dice_quantity)))
        print(f"*** {dice_string} ***")
        print(f"Enter dice to keep, or (q)uit:")
        game_input = input("> ")
# ** 1 1 4 1 3 2 **
# 1 1 1 2
        if game_input == "q":
          print(f"Thanks for playing. You earned {self.banker.balance} points")
          self.status = False
        else:
          get_score = GameLogic.calculate_score(game_input)
          self.banker.shelf(get_score)
          print(f"You have {self.banker.shelf} unbanked points and {dice_quantity} dice remaining")
          print("(r)oll again, (b)ank your points or (q)uit:")
          roll_again = input("> ")
          if roll_again == "r":
            print(f"Rolling {self.dice_quantity} dice...")
            continue
          if roll_again == "b":
            self.banker.bank()
            print(f"You banked {get_score} points in round {self.number_of_rounds}")
            self.number_of_rounds += 1
            self.banker.clear_shelf()
            break
          if roll_again == "q":
            pass

     
# You banked 50 points in round 1
# Total score is 50 points
     
# Banked points
# (r)oll again, (b)ank your points or (q)uit:
# user input
# total score
# start round 2
# Rolling {self.dice_quantity} dice...
# shows dice 
# Enter dice to keep, or (q)uit:
# user input
# Thanks for playing. You earned {}} points




  # def rolling(self, roller):


if __name__ == "__main__":
  play_game = Game()
  play_game.play()
