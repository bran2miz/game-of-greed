# test merge
# from random import choice, randit
import sys
from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic
# from game_of_greed.game_logic import GameLogic

class Game:

  def __init__(self):
    self.banker = Banker()
    self.status = True
    self.number_of_rounds = 0
    self.dice_quantity = 6

  def default_roller(self):
    GameLogic.roll_dice(self.dice_quantity)

  def play(self, roller= GameLogic.roll_dice):
    self.roll_dice = roller
    print("Welcome to Game of Greed")
    print("(y)es to play or (n)o to decline")
    while True:
      player_input = input("> ")
      if player_input == 'n':
        print('OK. Maybe another time')
        sys.exit()
      elif player_input == 'y':
        # self.dice_quantity = 6
        self.round_start(roller)
  


  def validate_dice(self, rolled_dice, roller):
    if GameLogic.calculate_score(rolled_dice) == 0:
      print('''
      ****************************************
      **        Zilch!!! Round over         **
      ****************************************
      ''')
      self.banker.clear_shelf()
      


  def round_start(self, roller):
    while self.status and self.banker.balance <= 10000:
      self.number_of_rounds += 1
      # while self.status:
      print(f"Starting round {self.number_of_rounds}")
      print(f"Rolling {self.dice_quantity} dice...")
# need to save the result from self.roll_dice to use in gamelogic.calulate_score
# dicerolled is the result of rolling the dice, used in dice_string and get_score
      dicerolled = roller(self.dice_quantity)
      # dice_string = str(dicerolled).strip("([])").replace(", ", " ")
      # dice_string = ''
      # for num in dicerolled:
      #   dice_string += str(num) + " "
      dice_string = ' '.join(str(num) for num in dicerolled)
      print(f"*** {dice_string} ***")
      print(f"Enter dice to keep, or (q)uit:")
 
      game_input = input("> " )
      # quitting
      if game_input == "q":
        print(f'Thanks for playing. You earned {self.banker.balance} points')
        # self.status = False
        sys.exit()
        
      # continuing the game
      else:
        user_entry = tuple(map(int, list(game_input)))
          # print('test line 1')
        self.dice_quantity -= len(user_entry)
        get_score = GameLogic.calculate_score(user_entry)
          # print('test line 2')
        self.banker.shelf(get_score)
# calculating dice quantity after user selects their dice
        
        print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
          
      # rolling again
        game_input = input("> ")
      # banking the points
        if game_input == "b":
          self.banker.bank()
          self.dice_quantity = 6
          print(f"You banked {get_score} points in round {self.number_of_rounds}")
          print(f"Total score is {self.banker.balance} points")
          # self.banker.clear_shelf()
          # self.number_of_rounds += 1
          # break

        elif game_input == "r":
          # self.number_of_rounds += 1
          if self.dice_quantity == 0:
            self.dice_quantity = 6
            # print(f"Rolling {self.dice_quantity} dice...")
          continue
      
        elif game_input == "q":
          print(f"Thanks for playing. You earned {self.banker.balance} points")
          sys.exit()

if __name__ == "__main__":
  play_game = Game()
  play_game.play()
 