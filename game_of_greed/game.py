import sys
from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic
# from game_of_greed.game_logic import GameLogic

class Game:

  def __init__(self, num_rounds=20):
    self.banker = Banker()
    self.number_of_rounds = 0
    self.num_rounds = num_rounds


  def play(self, roller= None):
    self.rolled = roller or GameLogic.roll_dice
    print("Welcome to Game of Greed")
    print("(y)es to play or (n)o to decline")
    # while True:
    player_input = input("> ")

    if player_input == 'n':
      print('OK. Maybe another time')

    else:
      for number_of_rounds in range(1, self.num_rounds + 1):
          self.round_start(number_of_rounds)
          
      self.quit_game()     
  
  def quit_game(self):
    print(f"Thanks for playing. You earned {self.banker.balance} points")
    sys.exit()
    
  def round_start(self, number_of_rounds):
      dice_quantity = 6
      print(f"Starting round {number_of_rounds}")
      farkle_score = 0
      # while self.status:
      while True:
        print(f"Rolling {dice_quantity} dice...")

        dicerolled = self.rolled(dice_quantity)
        dice_string = ' '.join([str(num) for num in dicerolled])
        print(f"*** {dice_string} ***")
        
        validate_score = GameLogic.calculate_score(dicerolled)
        
        if validate_score == 0:
            self.zilch(number_of_rounds)
            return
        
        keep_the_value = self.validate_keepers(dicerolled, dice_string)

        get_keeper_score = GameLogic.calculate_score(keep_the_value)

        farkle_score += get_keeper_score
        
        dice_quantity -= len(keep_the_value) 
        
        print(f"You have {farkle_score} unbanked points and {dice_quantity} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        # print(f"Enter dice to keep, or (q)uit:")
        player_input = input("> " )
        
        if player_input == "b":
            self.banker.shelf(farkle_score)
            banked_points = self.banker.bank()
            self.end_round(number_of_rounds, banked_points)
            break
        elif player_input == "r":
            if dice_quantity == 0:
                dice_quantity = 6
        elif player_input == "q":
            self.quit_game()

  def zilch(self, number_of_rounds):
      print("****************************************")
      print("**        Zilch!!! Round over         **")
      print("****************************************")
      
      self.end_round(number_of_rounds, 0)

  def end_round(self, number_of_rounds, banked_points):
    """bank points and finish round"""
    print(f"You banked {banked_points} points in round {number_of_rounds}")
    print(f"Total score is {self.banker.balance} points")

  def validate_keepers(self, dicerolled, dice_string):
    while True:
      print("Enter dice to keep, or (q)uit:")
      player_input = input("> ")
      if player_input == "q":
        self.quit_game()
        break

      keep_the_value = []
      for answer in player_input:
        if answer.isnumeric():
          keep_the_value.append(int(answer))

      if GameLogic.validate_keepers(dicerolled, keep_the_value):
        return keep_the_value
      else:
        print("Cheater!!! Or possibly made a typo...")
        print(f"*** {dice_string} ***")


if __name__ == "__main__":
  play_game = Game()
  play_game.play()