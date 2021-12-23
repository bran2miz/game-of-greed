import random
from collections import Counter

# 5’s = 50 points
# 1’s= 100 points

# 1,1,1 = 300 points
# 2,2,2 = 200 points
# 3,3,3 = 300 points
# 4,4,4 = 400 points
# 5,5,5 = 500 points
# 6,6,6 = 600 points

# Four of a Kind = 1,000 points
# Five of a Kind = 2,000 points
# Six of a Kind = 3,000 points
# A Straight of 1-6 = 1,500 points

# Three Pairs = 1,500 points
# Four of a Kind + a Pair = 1,500

# Two sets of Three of a Kind = 2,500


# Calculate Score -
#   input: tuple of integers as the dice roll
#   output: score from the roll
# what values could we tuple to find dice roll

# farkle = {(1,): 100),
#         ((1, 1): 200),
#         ((1, 1, 1): 1000),
#         ((1, 1, 1, 1): 2000),
#         ((1, 1, 1, 1, 1): 3000),
#         ((1, 1, 1, 1, 1, 1): 4000),
#         ((2,): 0),
#         ((2, 2): 0),
#         ((2, 2, 2): 200),
#         ((2, 2, 2, 2): 400),
#         ((2, 2, 2, 2, 2): 600),
#         ((2, 2, 2, 2, 2, 2): 800),
#         ((3,): 0),
#         ((3, 3): 0),
#         ((3, 3, 3): 300),
#         ((3, 3, 3, 3): 600),
#         ((3, 3, 3, 3, 3): 900),
#         ((3, 3, 3, 3, 3, 3): 1200),
#         ((4,): 0),
#         ((4, 4): 0),
#         ((4, 4, 4): 400),
#         ((4, 4, 4, 4): 800),
#         ((4, 4, 4, 4, 4): 1200),
#         ((4, 4, 4, 4, 4, 4): 1600),
#         ((5,): 50),
#         ((5, 5): 100),
#         ((5, 5, 5): 500),
#         ((5, 5, 5, 5): 1000),
#         ((5, 5, 5, 5, 5): 1500),
#         ((5, 5, 5, 5, 5, 5): 2000),
#         ((6,): 0),
#         ((6, 6): 0),
#         ((6, 6, 6): 600),
#         ((6, 6, 6, 6): 1200),
#         ((6, 6, 6, 6, 6): 1800),
#         ((6, 6, 6, 6, 6, 6): 2400),
#         ((1, 2, 3, 4, 5, 6): 1500),
#         ((2, 2, 3, 3, 4, 6): 0),
#         ((2, 2, 3, 3, 6, 6): 1500),
#         ((1, 1, 1, 2, 2, 2): 1200)
# }



class GameLogic:

    @staticmethod
    def calculate_score(roll_dice):
      # game_start = ()
      dice_number = Counter(roll_dice)
      print(dice_number)
      tally_score = 0

      # for i in game_start(1,7):
      #   if i == 1:
      #     tally_score += 50
      if dice_number[5] == 1:
        tally_score += 50 * dice_number[5]
      
      return tally_score

    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)