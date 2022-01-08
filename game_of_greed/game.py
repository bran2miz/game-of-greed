# # test merge
# # from random import choice, randit
# import sys
# from game_of_greed.banker import Banker
# from game_of_greed.game_logic import GameLogic
# # from game_of_greed.game_logic import GameLogic

# class Game:

#   def __init__(self):
#     self.banker = Banker()
#     self.status = True
#     self.number_of_rounds = 0
#     self.dice_quantity = 6

#   def default_roller(self):
#     GameLogic.roll_dice(self.dice_quantity)

#   def play(self, roller= None):
#     self.roll_dice = roller
#     print("Welcome to Game of Greed")
#     print("(y)es to play or (n)o to decline")
#     player_input = input("> ")
#     # While True:
#     if player_input == 'n':
#       print('OK. Maybe another time')
#       sys.exit()
#     elif player_input == 'y':
#       # self.dice_quantity = 6
#       self.round_start(roller)

#   def round_start(self, roller):
#     while self.status and self.banker.balance <= 10000:
#       self.number_of_rounds += 1
#       self.dice_quantity = 6
#       # while self.status:
#       print(f"Starting round {self.number_of_rounds}")
#       self.farkle_game(roller)

#   def farkle_game(self, roller):
#     rolled_dice = self.dice_roll(roller)
#     user_entry = self.dice_validator(rolled_dice, roller)
#     self.calculate_score(user_entry)
#     self.print_unbanked_and_dice_quantity()
#     self.bank_reroll_or_quit(roller)


#   def dice_roll(self, roller):
#     print(f"Rolling {self.dice_quantity} dice...")
#     dicerolled = roller(self.dice_quantity)
#     dice_string = ' '.join(str(num) for num in dicerolled)
#     print(f"*** {dice_string} ***")
#     return dicerolled

#   def dice_validator(self, rolled_dice, roller):
#     if GameLogic.calculate_score(rolled_dice) == 0:
#       print('''
#         ****************************************
#         **        Zilch!!! Round over         **
#         ****************************************
#         ''')
#       self.banker.clear_shelf(roller)
#     else:
#       print(f"Enter dice to keep, or (q)uit:")
#       game_input = input("> ")
#       if game_input == "q":
#         print(f"Thanks for playing. You earned {self.banker.balance} points")
#         sys.exit()
#       else:
#         user_entry = tuple(map(int, list(game_input)))
#           # print('test line 1')
#         validate_score = GameLogic.validate_keepers(rolled_dice, user_entry)
#         if validate_score == True:
#           return validate_score
#         else:
#           print("Cheater!!! Or possibly made a typo...")
#           print(f"*** {self.dice_string} ***")
#           return self.dice_validator(rolled_dice, roller)
#         # self.dice_quantity -= len(user_entry)
#         # get_score = GameLogic.calculate_score(user_entry)
#         #   # print('test line 2')
#         # self.banker.shelf(get_score)

#   def calculate_score(self, user_entry):
#     get_score = GameLogic.calculate_score(user_entry)
#     print(user_entry)
#     self.dice_quantity -= len(user_entry)
#     self.banker.shelf(get_score)
#     return get_score

#   def print_unbanked_and_dice_quantity(self):
#     print(f"You have {self.banker.shelved} unbanked points and {self.dice_quantity} dice remaining")

#   def bank_reroll_or_quit(self, roller):
#     print("(r)oll again, (b)ank your points or (q)uit:")
#     # rolling again
#     game_input = input("> ")

#     # banking the points
#     if game_input == "b":
#       self.banker.bank()
#       self.dice_quantity = 6
#       print(f"You banked {self.banker.shelved} points in round {self.number_of_rounds}")
#       print(f"Total score is {self.banker.balance} points")
#       # self.banker.clear_shelf()
#       # self.number_of_rounds += 1
#       # break

#     elif game_input == "r":
#       if self.dice_quantity == 0:
#         self.dice_quantity = 6
#         self.farkle_game(roller)
#       else:
#         self.farkle_game(roller)
      
#     elif game_input == "q":
#       print(f"Thanks for playing. You earned {self.banker.balance} points")
#       sys.exit()

import sys

from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0

    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
        else:
            for round_num in range(1, self.num_rounds + 1):
                self.start_round(round_num)

            self.end_game()

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def start_round(self, round_num):
        num_dice = 6
        print(f"Starting round {round_num}")
        round_score = 0

        while True:
            print(f"Rolling {num_dice} dice...")

            roll = self._roller(num_dice)
            roll_string = " ".join([str(value) for value in roll])
            print(f"*** {roll_string} ***")

            preliminary_score = GameLogic.calculate_score(roll)

            if preliminary_score == 0:
                self.zilch(round_num)
                return

            keeper_values = self.validate_keepers(roll, roll_string)

            keeper_score = GameLogic.calculate_score(keeper_values)

            round_score += keeper_score

            num_dice -= len(keeper_values)

            print(
                f"You have {round_score} unbanked points and {num_dice} dice remaining"
            )
            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")

            if response == "b":
                self.banker.shelf(round_score)
                banked_points = self.banker.bank()
                self.end_round(round_num, banked_points)
                break
            elif response == "r":
                if num_dice == 0:
                    num_dice = 6
            elif response == "q":
                self.end_game()

    def zilch(self, round_num):
        """Zero scoring dice were rolled so end round with 0 points"""
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

        self.end_round(round_num, 0)

    def end_round(self, round_num, banked_points):
        """bank points and finish round"""
        print(f"You banked {banked_points} points in round {round_num}")
        print(f"Total score is {self.banker.balance} points")

    def validate_keepers(self, roll, roll_string):
        """ensures that kept dice are valid for the roll
        Args:
            roll
            roll_string
        Returns:
            valid keeper values
        """
        while True:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "q":
                self.end_game()
                break

            keeper_values = []
            for char in response:
                if char.isnumeric():
                    keeper_values.append(int(char))

            if GameLogic.validate_keepers(roll, keeper_values):
                return keeper_values
            else:
                print("Cheater!!! Or possibly made a typo...")
                print(f"*** {roll_string} ***")


if __name__ == "__main__":
    game = Game()
    game.play()