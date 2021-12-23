import random
from collections import Counter



# Calculate Score -
#   input: tuple of integers as the dice roll
#   output: score from the roll
# what values could we tuple to find dice roll

# Straight 1-6	1,500
# Three Pairs	1,000 (2x2's, 2x3's, 2x4's, etc)
# 3x6's	600
# 4x6's	1,200
# 5x6's	2,400
# 6x6's	4,800
# unless rolled at one time then its automatic 10,000
# 3x5's	500
# 4x5's	1,000
# 5x5's	2,000
# 6x5's	4,000
# unless rolled at one time then its automatic 10,000
# 3x4's	400
# 4x4's	800
# 5x4's	1,600
# 6x4's	3,200
# unless rolled at one time then its automatic 10,000
# 3x3's	300
# 4x3's	600
# 5x3's	1,200
# 6x3's	2,400
# unless rolled at one time then its automatic 10,000
# 3x2's	200
# 4x2's	400
# 5x2's	800
# 6x2's	1,600
# unless rolled at one time then its automatic 10,000
# 3x1's	1,000
# 4x1's	2,000
# 5x1's	4,000
# 6x1's	8,000
# unless rolled at one time then its automatic 10,000

# If a player rolls all 6 of the same dice in 1 roll the game is automatically over no player gets a last roll.
# Double Trips when 2 sets of 3 of a kind are hit. Scores are added together and doubled.



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
      if dice_number[5] == 1 or dice_number[5]== 2:
        tally_score += 50 * dice_number[5]
      
      if dice_number[1] == 1 or dice_number[1] == 2:
        tally_score += 100 * dice_number[1]

      return tally_score

      

    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)