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
      tally_score = 0
      length_of_counter = len(dice_number)
      # print(f"{length_of_counter}")

    # Functions for 
    
      if dice_number[5] == 1 or dice_number[5]== 2:
        tally_score += 50 * dice_number[5]
        # print('adding 50')
      
      if dice_number[1] == 1 or dice_number[1] == 2:
        tally_score += 100 * dice_number[1]
        # print('adding 100')

    # Write a function that checks for three of a kind

      for i in range(1,7):
        if i == 1 and dice_number[1] == 3:
          tally_score += 1000
          # print('adding 1000')
        elif i != 1 and dice_number[i] == 3:
          tally_score += i * 100
          # print('adding 100')

    # Write a function that checks four of a kind
    # 1s = 2000, 2s = 400, 3s = 600, 4s = 800, 5s =1000, 6s = 1200

      for i in range(1,7):
        if i == 1 and dice_number[1] == 4:
          tally_score += 2000
          # print('adding 2000')
        elif i != 1 and dice_number[i] == 4:
          tally_score += i * 200
          # print('addding 200')

    # Write a function that checks five of a kind
    # 1s = 3000, 2s = 600, 3s = 900, 4s = 1200, 5s =1500, 6s = 1800

      for i in range(1,7):
        if i == 1 and dice_number[1] == 5:
          tally_score += 3000
          # print('adding 3000')
        elif i != 1 and dice_number[i] == 5:
          tally_score += i * 300
          # print('adding 300')

    # Write a function that checks six of a kind
    # 1s = 4000, 2s = 800, 3s = 1200, 4s = 1600, 5s =2000, 6s = 2400

      for i in range(1,7):
        if i == 1 and dice_number[1] == 6:
          tally_score += 4000
          # print('adding 4000')
        elif i != 1 and dice_number[i] == 6:
          tally_score += i * 400
          # print('adding 400')
         
    #Write a function that checks for a straight (1,2,3,4,5,6)

      for i in range(1,7):
        if length_of_counter == 6 and dice_number[i] == 1:
          tally_score = 1500
          # print('score 1500')

    # Write a function that checks for 3 pairs of 2


    # Write a function that checks for 2 pairs of 3
    # create a separate "tally score"
      tally_three_pair = 0

      for i in range(1,7):
        # if length_of_counter == 3 and dice_number[i] == 2:
        #   tally_score = 1500
        if dice_number[i] == 2:
          tally_three_pair += 1
        if tally_three_pair == 3:
          tally_score = 1500
          # print('score 1500')

      # print(f"{tally_score}")
      return tally_score
    #handles dice roll  
    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)

    # @staticmethod
    # def get_scorers():
    

    # @staticmethod
    # def validate_keepers(self, keeper, roller):

    
# legal_keepers
# illegal_keepers
# illegal_overflow 

