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

  def play(self, roller= None):
    self.roll_dice = roller
    print("Welcome to Game of Greed")
    print("(y)es to play or (n)o to decline")
    player_input = input("> ")
    # While True:
    if player_input == 'n':
      print('OK. Maybe another time')
    elif player_input == 'y':
      # self.dice_quantity = 6
      self.round_start(roller)

  def round_start(self, roller):
    while self.status and self.banker.balance <= 10000:
      self.number_of_rounds += 1
      self.dice_quantity = 6
      # while self.status:
      print(f"Starting round {self.number_of_rounds}")
      self.farkle_game(roller)

  def farkle_game(self, roller):
    rolled_dice = self.dice_roll(roller)
    user_entry = self.dice_validator(rolled_dice, roller)
    self.calculate_score(user_entry)
    self.print_unbanked_and_dice_quantity()
    self.bank_reroll_or_quit(roller)


  def dice_roll(self, roller):
    print(f"Rolling {self.dice_quantity} dice...")
    dicerolled = roller(self.dice_quantity)
    dice_string = ' '.join(str(num) for num in dicerolled)
    print(f"*** {dice_string} ***")
    return dicerolled

  def dice_validator(self, rolled_dice, roller):
    if GameLogic.calculate_score(rolled_dice) == 0:
      print('''
        ****************************************
        **        Zilch!!! Round over         **
        ****************************************
        ''')
      self.banker.clear_shelf()

  def calculate_score(self, user_entry):
    get_score = GameLogic.calculate_score(user_entry)
    print(user_entry)
    self.dice_quantity -= len(user_entry)
    self.banker.shelf(get_score)
    return get_score

  def print_unbanked_and_dice_quantity(self):
    print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")

  def bank_reroll_or_quit(self, roller):
    print("(r)oll again, (b)ank your points or (q)uit:")
    # rolling again
    game_input = input("> ")

    # banking the points
    if game_input == "b":
      self.banker.bank()
      self.dice_quantity = 6
      print(f"You banked {self.banker.shelved} points in round {self.number_of_rounds}")
      print(f"Total score is {self.banker.balance} points")
      # self.banker.clear_shelf()
      # self.number_of_rounds += 1
      # break

    elif game_input == "r":
      if self.dice_quantity == 0:
        self.dice_quantity = 6
        self.farkle_game(roller)
      else:
        self.farkle_game(roller)
      
    elif game_input == "q":
      print(f"Thanks for playing. You earned {self.banker.balance} points")
      sys.exit()