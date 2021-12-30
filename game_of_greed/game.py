from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic
# from game_of_greed.game_logic import GameLogic

class Game:

  def __init__(self, rounds = 1, dice_quantity = 6):
    self.banker = Banker()
    self.status = True
    self.number_of_rounds = rounds
    self.roll_dice = GameLogic.roll_dice
    self.dice_quantity = dice_quantity

  def play(self, roller = None):
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
        print("Starting round {self.number_of_rounds}")
        print("Rolling {self.dice_quantity} dice...")
        dice_string = ''.join(str(num) for num in (self.roll_dice(self.dice_quantity)))
        print(f"*** {dice_string} ***")
        print(f"Enter dice to keep, or (q)uit:")
        quit_game = input("> ")

        if quit_game == 'q':
          print("Thanks for playing. You earned {self.banker.balance} points")
     



  # def rolling(self, roller):


if __name__ == "__main__":
  play_game = Game()
  play_game.play()








# Application should simulate rolling between 1 and 6 dice
    # rolling function - everything needs access to this function
    # for print: concatenate dice #s with the ***


# Application should allow user to set aside dice each roll
    # shelving dice 
  
# Application should keep track of current round
    # rounds need a start point then increase after each roll

# Application should allow 'banking' current score or rolling again.
# Application should keep track of total score

# Application should implement all features from previous version
# Application should have automated tests to ensure proper operation